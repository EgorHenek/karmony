"""Cryptocurrency trackers."""

from abc import ABC, abstractmethod

from aiohttp import ClientSession


class TrackerError(Exception):
    """The base exception for all tracker errors."""


class Tracker(ABC):
    """An abstract tracker."""

    def __init__(self, session: ClientSession) -> None:
        """Create a new Tracker instance."""
        super().__init__()
        self._session = session

    @abstractmethod
    async def get_token_price(
        self,
        symbol: str,
        currency: str = "USD",
    ) -> float:
        """Get the price of a token."""


class CoinMarketCapTracker(Tracker):
    """CoinMarketCap.com."""

    def __init__(self, session: ClientSession, api_key: str) -> None:
        """Create a new CoinMarketCapTracker instance."""
        super().__init__(session)
        self._api_key = api_key
        self._base_url = "https://pro-api.coinmarketcap.com"

    async def get_token_price(
        self,
        symbol: str,
        currency: str = "USD",
    ) -> float:
        """Get the price of a token."""
        params = {
            "amount": 1,
            "symbol": symbol,
            "convert": currency,
        }

        async with self._session.get(
            f"{self._base_url}/v2/tools/price-conversion",
            params=params,
            headers={"X-CMC_PRO_API_KEY": self._api_key},
        ) as request:
            data = await request.json()
            if request.status == 200:  # noqa: PLR2004
                return data["data"][symbol]["quote"][currency]["price"]
            msg = f"{data['status']['error_message']}: {data['status']['error_message']}"
            raise TrackerError(msg)


class CoinGeckoTracker(Tracker):
    """CoinGecko.com."""

    def __init__(self, session: ClientSession, api_key: str = "") -> None:
        """Create a new CoinGeckoTracker instance."""
        super().__init__(session)
        self._api_key = api_key
        self._base_url = "https://api.coingecko.com"

    async def get_token_price(
        self,
        symbol: str,
        currency: str = "USD",
    ) -> float:
        """Get the price of a token."""
        symbol = symbol.lower()
        currency = currency.lower()

        params = {
            "ids": symbol,
            "vs_currencies": currency,
        }

        async with self._session.get(
            f"{self._base_url}/api/v3/simple/price",
            params=params,
            headers={
                "x-cg-demo-api-key": self._api_key,
            },
        ) as request:
            data = await request.json()
            if request.status == 200:  # noqa: PLR2004
                return float(data[symbol][currency])
            raise TrackerError
