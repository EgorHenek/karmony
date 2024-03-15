from typing import AsyncGenerator

import pytest
from aiohttp import ClientSession


@pytest.fixture
def anyio_backend():
    return "asyncio"


@pytest.fixture(name="session")
async def session_fixture() -> AsyncGenerator[ClientSession, None]:
    async with ClientSession() as session:
        yield session
