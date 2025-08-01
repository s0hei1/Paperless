import pytest
from httpx import AsyncClient

from apps.paperless.api.route_path.route_path import Routes
from global_fixture import app, async_client
from fixtures import create_user_request

@pytest.mark.asyncio
async def test_create_user(
        async_client : AsyncClient,
        create_user_request : dict
):
    create_user = await async_client.post(Routes.User.create.url, json=create_user_request)
    create_user.raise_for_status()

    assert all([i in  create_user.json() for i in ['user_name', 'first_name', 'last_name', 'user_roll', 'department_id']])
