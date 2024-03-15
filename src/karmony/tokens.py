from __future__ import annotations

from karmony.exceptions import ContractAddressNotFoundError


class Token:
    """Abstract token."""

    def __init__(
        self,
        network_addresses: dict[str, str],
    ) -> None:
        """Token constructor."""
        self._network_addresses = network_addresses

    @property
    def name(self) -> str:
        """The name property."""
        return self.__class__.__name__

    def get_address(self, network: str) -> str:
        """Get address for network."""
        address = self._network_addresses.get(network)
        if not address:
            msg = f"Token {self.name} not found for network {network}"
            raise ContractAddressNotFoundError(msg)
        return self._network_addresses[network]


Matic = Token(
    {
        "Polygon": "0x0000000000000000000000000000000000001010",
        "Polygon Mumbai": "0x0000000000000000000000000000000000001010",
    },
)

USDT = Token(
    {
        "Ethereum": "0xdAC17F958D2ee523a2206206994597C13D831ec7",
        "Avalanche": "0x9702230A8Ea53601f5cD2dc00fDBc13d4dF4A8c7",
        "Arbitrum": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
        "Optimism": "0x94b008aa00579c1307b0ef2c499ad98a8ce58e58",
        "Polygon": "0xc2132D05D31c914a87C6611C10748AEb04B58e8F",
        "ZkSync": "0x493257fD37EDB34451f62EDf8D2a0C418852bA4C",
        "Linea": "0xA219439258ca9da29E9Cc4cE5596924745e12B93",
        "Scroll": "0xf55BEC9cafDbE8730f096Aa55dad6D22d44099Df",
        "BNB Smart Chain": "0x55d398326f99059ff775485246999027b3197955",
        "Manta": "0xf417F5A458eC102B90352F697D6e2Ac3A3d2851f",
    }
)

USDC = Token(
    {
        "Ethereum": "0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48",
        "Avalanche": "0xB97EF9Ef8734C71904D8002F8b6Bc66DD9c48a6E",
        "Arbitrum": "0xaf88d065e77c8cC2239327C5EDb3A432268e5831",
        "Optimism": "0x0b2C639c533813f4Aa9D7837CAf62653d097Ff85",
        "Polygon": "0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359",
        "ZkSync": "0x3355df6d4c9c3035724fd0e3914de96a5a83aaf4",
        "Base": "0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913",
        "Linea": "0x176211869cA2b568f2A7D4EE941E073a821EE1ff",
        "Scroll": "0x06eFdBFf2a14a7c8E15944D1F4A48F9F95F663A4",
        "BNB Smart Chain": "0x8ac76a51cc950d9822d68b83fe1ad97b32cd580d",
        "Manta": "0xb73603C5d87fA094B7314C74ACE2e64D165016fb",
        "Polygon Mumbai": "0x0FA8781a83E46826621b3BC094Ea2A0212e71B23",
    }
)

ETH = Token(
    {
        "Ethereum": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "Arbitrum": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "Arbitrum Nova": "0x722E8BdD2ce80A4422E880164f2079488e115365",
        "Zora": "0x4200000000000000000000000000000000000006",
        "Optimism": "0x4200000000000000000000000000000000000006",
        "Polygon": "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
        "Base": "0x4200000000000000000000000000000000000006",
        "Linea": "0xe5D7C2a44FfDDf6b295A15c148167daaAf5Cf34f",
        "Scroll": "0x5300000000000000000000000000000000000004",
        "Manta": "0x0Dc808adcE2099A9F62AA87D9670745AbA741746",
    }
)

WETH = Token(
    {
        "Ethereum": "0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2",
        "Arbitrum": "0x82aF49447D8a07e3bd95BD0d56f35241523fBab1",
        "Arbitrum Nova": "0x722E8BdD2ce80A4422E880164f2079488e115365",
        "Zora": "0x4200000000000000000000000000000000000006",
        "Optimism": "0x4200000000000000000000000000000000000006",
        "Polygon": "0x7ceB23fD6bC0adD59E62ac25578270cFf1b9f619",
        "Base": "0x4200000000000000000000000000000000000006",
        "Scroll": "0x5300000000000000000000000000000000000004",
        "Manta": "0x0Dc808adcE2099A9F62AA87D9670745AbA741746",
    }
)
