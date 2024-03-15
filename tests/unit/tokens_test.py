import pytest

from karmony.exceptions import ContractAddressNotFoundError
from karmony.tokens import Token


class TestToken:
    @pytest.fixture
    def token(self) -> Token:
        return Token(
            {
                "Test": "0x0000000000000000000000000000000000001010",
            }
        )

    def test_name(
        self,
        token: Token,
    ) -> None:
        assert token.name == "Token"

    def test_get_address(self, token: Token) -> None:
        address = token.get_address("Test")

        assert address == "0x0000000000000000000000000000000000001010"

    def test_get_unknown_address(self, token: Token) -> None:
        with pytest.raises(ContractAddressNotFoundError):
            token.get_address("Test2")
