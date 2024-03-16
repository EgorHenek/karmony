from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass
class BaseNetwork:
    rpc: str
    chain_id: int

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
