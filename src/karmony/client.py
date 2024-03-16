from __future__ import annotations

from typing import TYPE_CHECKING

from web3 import AsyncHTTPProvider, AsyncWeb3
from web3.types import Nonce, Wei

from karmony.exceptions import MaxAddittionalNonceCounterReachedError, NonRepeatableError

if TYPE_CHECKING:
    from eth_account.account import SignedTransaction
    from eth_account.signers.local import LocalAccount
    from hexbytes import HexBytes
    from web3.types import TxParams

    from karmony.networks import BaseNetwork


class EvmClient:
    def __init__(self, network: BaseNetwork) -> None:
        self._client = AsyncWeb3(AsyncHTTPProvider(network.rpc))
        self._network = network

    async def transfer(
        self,
        signer: LocalAccount,
        to: str,
        value: Wei,
        max_fee_per_gas: Wei | None = None,
        max_priority_fee_per_gas: Wei | None = None,
        max_addittional_nonce_count=10,
    ) -> HexBytes:
        nonce = await self._client.eth.get_transaction_count(signer.address)

        if not max_fee_per_gas:
            block = await self._client.eth.get_block("latest")
            if "baseFeePerGas" not in block:
                msg = "Fee data is not available"
                raise NonRepeatableError(msg)
            max_fee_per_gas = block["baseFeePerGas"]

        tx: TxParams = {
            "from": signer.address,
            "to": to,
            "value": value,
            "gas": 21000,
            "nonce": nonce,
            "maxFeePerGas": max_fee_per_gas,
            "maxPriorityFeePerGas": max_priority_fee_per_gas if max_priority_fee_per_gas else Wei(1000000000),
        }

        while max_addittional_nonce_count > 0:
            try:
                return await self._send_transaction(tx, signer)
            except ValueError as e:
                if str(e) == "{'code': -32000, 'message': 'replacement transaction underpriced'}":
                    tx["nonce"] = Nonce(tx["nonce"] + 1)
                    max_addittional_nonce_count -= 1
                    continue
        raise MaxAddittionalNonceCounterReachedError

    async def wait_for_tx(self, tx_hash: HexBytes) -> None:
        await self._client.eth.wait_for_transaction_receipt(tx_hash)

    async def _send_transaction(self, tx: TxParams, signer: LocalAccount) -> HexBytes:
        signed_tx = self._sign_transaction(tx, signer)
        return await self._client.eth.send_raw_transaction(signed_tx.rawTransaction)

    def _sign_transaction(self, tx: TxParams, signer: LocalAccount) -> SignedTransaction:
        tx["chainId"] = self._network.chain_id
        return self._client.eth.account.sign_transaction(tx, signer.key)
