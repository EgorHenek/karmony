from __future__ import annotations

from typing import TYPE_CHECKING, Literal

from web3 import AsyncHTTPProvider, AsyncWeb3
from web3.middleware.geth_poa import async_geth_poa_middleware
from web3.types import FeeHistory, Nonce, Wei

from karmony.exceptions import MaxAddittionalNonceCounterReachedError

if TYPE_CHECKING:
    from eth_account.datastructures import SignedTransaction
    from eth_account.signers.local import LocalAccount
    from hexbytes import HexBytes
    from web3.types import TxParams

    from karmony.networks import BaseNetwork

REPLACE_ERROR_MESSAGES = {
    "INTERNAL_ERROR: could not replace existing tx",
    "replacement transaction underpriced",
}

_RPC_ERROR_CODE = -32000
_FEE_STRATEGIES = Literal["low", "medium", "high"]


class EvmClient:
    def __init__(self, network: BaseNetwork, *, timeout: int = 60) -> None:
        self._client = AsyncWeb3(AsyncHTTPProvider(network.rpc, request_kwargs={"timeout": timeout}))
        self._client.middleware_onion.inject(async_geth_poa_middleware, layer=0)
        self._network = network

    async def transfer(
        self,
        signer: LocalAccount,
        to: str,
        value: Wei,
        gas_price: Wei | None = None,
        max_fee_per_gas: Wei | None = None,
        max_priority_fee_per_gas: Wei | None = None,
        max_addittional_nonce_count=10,
        *,
        strategy: _FEE_STRATEGIES = "low",
    ) -> HexBytes:
        nonce = await self._client.eth.get_transaction_count(signer.address)

        tx: TxParams = {
            "from": signer.address,
            "to": to,
            "value": value,
            "gas": 0,
            "nonce": nonce,
        }

        if self._network.has_eip_1559_support:
            if not max_fee_per_gas or not max_priority_fee_per_gas:
                fees = await self._calculate_fees(strategy)
                max_priority_fee_per_gas = (
                    max_priority_fee_per_gas if max_priority_fee_per_gas else fees["maxPriorityFeePerGas"]
                )
                max_fee_per_gas = (
                    max_fee_per_gas if max_fee_per_gas else Wei(fees["baseFeePerGas"] + max_priority_fee_per_gas)
                )

            tx["maxFeePerGas"] = max_fee_per_gas
            tx["maxPriorityFeePerGas"] = max_priority_fee_per_gas
        else:
            if not gas_price:
                gas_price = await self._client.eth.gas_price
            tx["gasPrice"] = gas_price

        tx["gas"] = await self._client.eth.estimate_gas(tx)
        while max_addittional_nonce_count > 0:
            try:
                return await self._send_transaction(tx, signer)
            except ValueError as e:
                if e.args[0]["code"] == _RPC_ERROR_CODE and e.args[0]["message"] in REPLACE_ERROR_MESSAGES:
                    tx["nonce"] = Nonce(tx["nonce"] + 1)
                    max_addittional_nonce_count -= 1
                    continue
                raise
        raise MaxAddittionalNonceCounterReachedError

    async def wait_for_tx(self, tx_hash: HexBytes) -> None:
        await self._client.eth.wait_for_transaction_receipt(tx_hash)

    async def _send_transaction(self, tx: TxParams, signer: LocalAccount) -> HexBytes:
        signed_tx = self._sign_transaction(tx, signer)
        return await self._client.eth.send_raw_transaction(signed_tx.rawTransaction)

    def _sign_transaction(self, tx: TxParams, signer: LocalAccount) -> SignedTransaction:
        tx["chainId"] = self._network.chain_id
        return self._client.eth.account.sign_transaction(tx, signer.key)

    async def _calculate_fees(
        self,
        strategy: Literal["low", "medium", "high"] = "low",
    ) -> dict[str, Wei]:
        history = await self._client.eth.fee_history(4, "pending", [25, 50, 75])

        result = {"baseFeePerGas": Wei(0), "maxPriorityFeePerGas": Wei(0)}

        priority = await self._calculate_priority_fees(history)
        result["maxPriorityFeePerGas"] = Wei(max(priority[strategy]))

        base = await self._calculate_base_fee(history)
        result["baseFeePerGas"] = base

        return result

    async def _calculate_base_fee(self, history: FeeHistory) -> Wei:
        return Wei(max(history["baseFeePerGas"]))

    async def _calculate_priority_fees(
        self,
        history: FeeHistory,
    ) -> dict[_FEE_STRATEGIES, list[Wei]]:
        rewards: dict[_FEE_STRATEGIES, list[Wei]] = {
            "low": [],
            "medium": [],
            "high": [],
        }
        for reward in history["reward"]:
            rewards["low"].append(reward[0])
            rewards["medium"].append(reward[1])
            rewards["high"].append(reward[2])
        return rewards
