import pytest
from eth_account.account import LocalAccount
from web3.types import Wei

from karmony.client import EvmClient


class TestEvmClient:
    @pytest.mark.anyio
    @pytest.mark.slow
    async def test_send_transaction(
        self,
        sepolia_client: EvmClient,
        account: LocalAccount,
    ) -> None:
        await sepolia_client.transfer(
            account,
            "0x0000000000000000000000000000000000000000",
            Wei(0),
        )
