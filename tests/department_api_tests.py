import pytest
from httpx import AsyncClient
from apps.paperless.api.route_path.route_path import Routes
from global_fixture import app, async_client
from fixtures import fake_department_create_request

@pytest.mark.asyncio
async def test_create_department(
        async_client: AsyncClient,
        fake_department_create_request: dict
):
    response = await async_client.post(Routes.Department.create.url, json=fake_department_create_request)
    response.raise_for_status()

    data = response.json()
    assert all(field in data for field in ['id', 'name', 'code'])


@pytest.mark.asyncio
async def test_read_one_department(
        async_client: AsyncClient,
        fake_department_create_request: dict
):
    create_response = await async_client.post(Routes.Department.create.url, json=fake_department_create_request)
    create_response.raise_for_status()
    department_id = create_response.json().get("id")

    read_response = await async_client.get(Routes.Department.read_one.url, params={"id": department_id})
    read_response.raise_for_status()

    data = read_response.json()
    assert data["id"] == department_id
    assert all(field in data for field in ['id', 'name', 'code'])


@pytest.mark.asyncio
async def test_read_many_departments(
        async_client: AsyncClient
):
    response = await async_client.get(Routes.Department.read_many.url)
    response.raise_for_status()

    departments = response.json()
    assert isinstance(departments, list)
    if departments:
        assert all(field in departments[0] for field in ['id', 'name', 'code'])


@pytest.mark.asyncio
async def test_update_department(
        async_client: AsyncClient,
        fake_department_create_request: dict
):
    # Create
    create_response = await async_client.post(Routes.Department.create.url, json=fake_department_create_request)
    create_response.raise_for_status()
    department = create_response.json()

    # Modify and update
    department['name'] = "Updated Department Name"
    update_response = await async_client.put(Routes.Department.update.url, json=department, params={"id": department["id"]})
    update_response.raise_for_status()

    updated = update_response.json()
    assert updated["name"] == "Updated Department Name"
    assert all(field in updated for field in ['id', 'name', 'code'])


@pytest.mark.asyncio
async def test_delete_department(
        async_client: AsyncClient,
        fake_department_create_request: dict
):
    # Create
    create_response = await async_client.post(Routes.Department.create.url, json=fake_department_create_request)
    create_response.raise_for_status()
    department_id = create_response.json()["id"]

    # Delete
    delete_response = await async_client.delete(Routes.Department.delete.url, params={"id": department_id})
    delete_response.raise_for_status()

    data = delete_response.json()
    assert data.get("id") == department_id
    assert "message" in data
