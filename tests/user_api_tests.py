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


@pytest.mark.asyncio
async def test_read_one_user(
        async_client: AsyncClient,
        create_user_request: dict
):
    create_user = await async_client.post(Routes.User.create.url, json=create_user_request)
    create_user.raise_for_status()

    read_user = await async_client.get(Routes.User.read_one.url, params= {"id" : create_user["id"]})
    read_user.raise_for_status()

    assert all([i in  create_user.json() for i in ['user_name', 'first_name', 'last_name', 'user_roll', 'department_id']])

@pytest.mark.asyncio
async def test_read_many_users(
        async_client: AsyncClient,
        create_user_request: dict
):
    read_users = await async_client.get(Routes.User.read_many.url)
    read_users.raise_for_status()

    assert isinstance(read_users.json(), list)

@pytest.mark.asyncio
async def test_update_user(
        async_client: AsyncClient,
        create_user_request: dict
):
    create_user = await async_client.post(Routes.User.create.url, json=create_user_request)
    create_user.raise_for_status()
    user = create_user.json()

    user['first_name'] = "Updated Maryam"

    update_user = await async_client.put(Routes.User.update.url, json=user)

@pytest.mark.asyncio
async def test_delete_user(
        async_client: AsyncClient,
        create_user_request: dict
):
    create_user = await async_client.post(Routes.User.create.url, json=create_user_request)
    create_user.raise_for_status()

    response = await async_client.delete(Routes.User.delete.url, params={"id" : create_user.json().get("id")})
    response.raise_for_status()

    assert response.json().get("id") == create_user.json().get("id")
    assert response.json().get("message")
