from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass
class BaseNetwork:
    rpc: str
    chain_id: int
    has_eip_1559_support: bool = True

    def __post_init__(self) -> None:
        self.validate_rpc()

    def validate_rpc(self) -> None:
        parsed_url = urlparse(self.rpc)
        if parsed_url.scheme not in ["http", "https"]:
            msg = "RPC address must have 'http' or 'https' scheme"
            raise ValueError(msg)


class Sepolia(BaseNetwork):
    def __init__(self, rpc: str = "https://rpc2.sepolia.org") -> None:
        super().__init__(rpc, 11155111)


class Ethereum(BaseNetwork):
    def __init__(self, rpc: str = "https://rpc.ankr.com/eth") -> None:
        super().__init__(rpc, 1)


class BSC(BaseNetwork):
    def __init__(self, rpc: str = "https://bsc-dataseed1.binance.org/") -> None:
        super().__init__(rpc, 56)


class BSCTestnet(BaseNetwork):
    def __init__(
        self,
        rpc: str = "https://data-seed-prebsc-1-s1.binance.org:8545/",
    ) -> None:
        super().__init__(rpc, 97)


class PolygonMumbai(BaseNetwork):
    def __init__(self, rpc: str = "https://rpc.ankr.com/polygon_mumbai") -> None:
        super().__init__(rpc, 80001)


class Polygon(BaseNetwork):
    def __init__(self, rpc: str = "https://polygon-rpc.com") -> None:
        super().__init__(rpc, 137)


class ScrollSepolia(BaseNetwork):
    def __init__(self, rpc: str = "https://sepolia-rpc.scroll.io") -> None:
        super().__init__(rpc, 534351, False)


class Scroll(BaseNetwork):
    def __init__(self, rpc: str = "https://rpc.scroll.io") -> None:
        super().__init__(rpc, 534352, False)


class ZkSyncSepolia(BaseNetwork):
    def __init__(self, rpc: str = "https://sepolia.era.zksync.dev") -> None:
        super().__init__(rpc, 300)


class ZkSync(BaseNetwork):
    def __init__(self, rpc: str = "https://mainnet.era.zksync.io") -> None:
        super().__init__(rpc, 324)


class ArbitrumSepolia(BaseNetwork):
    def __init__(self, rpc="https://sepolia-rollup.arbitrum.io/rpc") -> None:
        super().__init__(rpc, 421614)


class Arbitrum(BaseNetwork):
    def __init__(self, rpc="https://arb1.arbitrum.io/rpc") -> None:
        super().__init__(rpc, 42161)


class ArbitrumNova(BaseNetwork):
    def __init__(self, rpc="https://nova.arbitrum.io/rpc") -> None:
        super().__init__(rpc, 42170)


class Base(BaseNetwork):
    def __init__(self, rpc="https://mainnet.base.org") -> None:
        super().__init__(rpc, 8453)


class BaseSepolia(BaseNetwork):
    def __init__(self, rpc="https://sepolia.base.org") -> None:
        super().__init__(rpc, 84532)


class Zora(BaseNetwork):
    def __init__(self, rpc="https://rpc.zora.energy") -> None:
        super().__init__(rpc, 7777777, False)


class ZoraSepolia(BaseNetwork):
    def __init__(self, rpc="https://sepolia.rpc.zora.energy") -> None:
        super().__init__(rpc, 999999999, False)
