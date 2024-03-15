import pytest
from aiohttp import ClientSession

from karmony.trackers import CoinGeckoTracker, CoinMarketCapTracker


class CoinMarketCapSandbox(CoinMarketCapTracker):
    def __init__(
        self,
        session: ClientSession,
    ) -> None:
        super().__init__(session, "b54bcf4d-1bca-4e8e-9a24-22ff2c3d462c")
        self._base_url = "https://sandbox-api.coinmarketcap.com"


class TestCoinMarketCap:
    @pytest.fixture
    def tracker(
        self,
        session: ClientSession,
    ) -> CoinMarketCapSandbox:
        return CoinMarketCapSandbox(session)

    @pytest.mark.anyio
    async def test_get_token_price(
        self,
        tracker: CoinMarketCapSandbox,
    ) -> None:
        price = await tracker.get_token_price("USDT")

        assert price


class TestCoinGecko:
    @pytest.fixture
    def tracker(
        self,
        session: ClientSession,
    ) -> CoinGeckoTracker:
        return CoinGeckoTracker(session)

    @pytest.mark.anyio
    async def test_get_token_price(
        self,
        tracker: CoinGeckoTracker,
    ) -> None:
        price = await tracker.get_token_price("bitcoin")

        assert price
