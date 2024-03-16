import os

import pytest
from eth_account.account import Account, LocalAccount

from karmony.client import EvmClient
from karmony.networks import BaseNetwork, Sepolia


@pytest.fixture
def network() -> BaseNetwork:
    return Sepolia()


@pytest.fixture
def private_key() -> str:
    key = os.environ.get("PRIVATE_KEY")
    if not key:
        msg = "PRIVATE_KEY not set"
        raise ValueError(msg)
    return key


@pytest.fixture
def account(private_key: str) -> LocalAccount:
    return Account.from_key(private_key)


@pytest.fixture
def sepolia_client(
    network: BaseNetwork,
) -> EvmClient:
    return EvmClient(network)
