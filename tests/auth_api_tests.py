import pytest
from fastapi import FastAPI
from httpx import AsyncClient
from apps.paperless.api.route_path.route_path import Routes
from global_fixture import app, async_client
from fixtures import create_user_request,fake_fail_login_request

@pytest.mark.asyncio
async def test_success_login(
        app : FastAPI,
        async_client : AsyncClient,
        create_user_request: dict):
    create_user =await async_client.post(Routes.User.create.url,json=create_user_request)
    create_user.raise_for_status()

    login_request = {
        "user_name" : create_user_request['user_name'],
        "password" : create_user_request['password'],
    }

    login_response = await async_client.post(Routes.Auth.login.url , json=login_request)
    login_response.raise_for_status()

    assert login_response.json().get("token")

@pytest.mark.asyncio
async def test_login_fails(
        app : FastAPI,
        async_client : AsyncClient,
        fake_fail_login_request : dict
):
    response =await async_client.post("/auth/login",data=fake_fail_login_request)
    assert not response.is_success
    assert response.json().get("message")

