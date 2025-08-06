import pytest
from random import randint


@pytest.fixture()
def create_user_request() -> dict:
    any_int = randint(0, 1000)
    return {
        'first_name': f'maryam',
        'last_name': f'p',
        'user_name': f'testuser_{any_int}',
        'password': 'test_password',
        'user_roll': 1,
        "department_id": 1,
    }


@pytest.fixture()
def fake_fail_login_request() -> dict:
    return {
        'username': 'testuser',
        'password': 'wrong_password'
    }


@pytest.fixture()
def fake_department_create_request():
    any_int = randint(100, 999)
    return {
        "name": f"Test Department_{any_int}",
        "code": any_int
    }


@pytest.fixture()
def fake_goods_exit_doc_create_request():
    return {
        "doc_date": "2025-05-05",
        "sending_department_id": 1,
        "exit_reason": "Its a Garbage",
        "destination": "Recycle bin",
        "address": "Moon",
        "exit_for_ever": True,
        "receiver_name": "Soheil",
        "approver_guard_id": 1,
        "approver_manager_id": 1,
        "items": [
            {
                "description": "Motor 3 Phase",
                "count": "6",
                "unit_of_measure_id": 1,
            },
            {
                "description": "Shafts",
                "sap_code": "12123",
                "count": "10",
                "unit_of_measure_id": 1,
            },
        ]
    }


@pytest.fixture()
def fake_approve_doc():
    pass
