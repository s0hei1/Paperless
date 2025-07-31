import pytest
from random import randint


@pytest.fixture()
def create_user_request() -> dict:
    any_int = randint(0, 1000)
    return {
        'first_name': f'maryam',
        'last_name': f'p',
        'username': f'testuser_{any_int}',
        'password' : 'test_password',
        'user_roll' : 1
    }

@pytest.fixture()
def fake_fail_login_request() -> dict:
    return {
        'username': 'testuser',
        'password' : 'wrong_password'
    }
