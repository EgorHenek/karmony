import os

import pytest
from eth_account.account import Account
from eth_account.signers.local import LocalAccount

from karmony.client import EvmClient
from karmony.networks import BSCTestnet, PolygonMumbai, ScrollSepolia, Sepolia, ZkSyncSepolia


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
def sepolia_client() -> EvmClient:
    return EvmClient(network=Sepolia())


@pytest.fixture
def bsc_testnet_client() -> EvmClient:
    return EvmClient(network=BSCTestnet())


@pytest.fixture
def polygon_mumbai_client() -> EvmClient:
    return EvmClient(network=PolygonMumbai())


@pytest.fixture
def scroll_sepolia_client() -> EvmClient:
    return EvmClient(network=ScrollSepolia())


@pytest.fixture
def zksync_sepolia_client() -> EvmClient:
    return EvmClient(network=ZkSyncSepolia())
