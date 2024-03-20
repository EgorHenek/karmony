from typing import TYPE_CHECKING

import pytest
from eth_account.signers.local import LocalAccount
from web3.types import Wei

if TYPE_CHECKING:
    from karmony.client import EvmClient


@pytest.mark.parametrize(
    "network",
    [
        "sepolia",
        "bsc_testnet",
        "polygon_mumbai",
        "scroll_sepolia",
        "zksync_sepolia",
        "arbitrum_sepolia",
        "base_sepolia",
        "zora_sepolia",
    ],
)
class TestEvmClient:
    @pytest.mark.anyio
    @pytest.mark.slow
    async def test_send_transaction(
        self,
        account: LocalAccount,
        request: pytest.FixtureRequest,
        network: str,
    ) -> None:
        client: EvmClient = request.getfixturevalue(f"{network}_client")
        assert await client.transfer(
            account,
            "0x3c77984a967702Efcd9A80B230c20e805c02F751",
            Wei(0),
        )
