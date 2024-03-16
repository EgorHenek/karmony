import pytest

from karmony.networks import BaseNetwork


class TestBaseNetwork:
    def test_rpc_address_validate(self) -> None:
        with pytest.raises(ValueError, match="RPC address must have 'http' or 'https' scheme"):
            BaseNetwork("wss://badnetwork", 1)
