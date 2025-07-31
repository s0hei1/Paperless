import pytest
from fastapi import FastAPI
from httpx import AsyncClient, ASGITransport

@pytest.fixture
def app() -> FastAPI:
    return FastAPI()

@pytest.fixture
def async_client(app: FastAPI) -> AsyncClient:
    async def async_client(app: FastAPI) -> AsyncClient:
        async with AsyncClient(
                transport=ASGITransport(app=app),
                base_url="http://test/"
        ) as client:
            yield client

