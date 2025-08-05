import pytest
from httpx import AsyncClient
from apps.paperless.api.route_path.route_path import Routes
from global_fixture import  app,async_client
from fixtures import fake_goods_exit_doc_create_request,create_user_request, fake_department_create_request

@pytest.mark.asyncio
async def test_create_goods_exit_doc(
        async_client : AsyncClient,
        create_user_request : dict,
        fake_goods_exit_doc_create_request : dict,
        fake_department_create_request : dict,
):

    create_user = await async_client.post(Routes.User.create.url, json=create_user_request)
    create_user.raise_for_status()

    department_response = await async_client.post(Routes.Department.create.url, json=fake_department_create_request)
    department_response.raise_for_status()

    department = department_response.json()

    fake_goods_exit_doc_create_request['sending_department_id'] = department['id']

    login_request = {
        'user_name': create_user_request['user_name'],
        'password': create_user_request['password'],
    }

    token_response = await async_client.post(Routes.Auth.login.url, json=login_request)
    token_response.raise_for_status()

    token = token_response.json().get('token')

    async_client.headers.update({
        'Authorization': f'Bearer {token}'
    })

    response = await async_client.post(Routes.GoodsExitDoc.create.url, json = fake_goods_exit_doc_create_request)
    print(response.json())
    response.raise_for_status()






