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
