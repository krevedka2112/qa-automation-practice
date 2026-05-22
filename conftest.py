import json
import os
from http import HTTPStatus

import pytest
import requests
from faker import Faker

from api.client import Client
from utils.login_page import LoginPage


@pytest.fixture(scope="session")
def config():
    root_path = os.path.dirname(os.path.abspath("config.json"))
    config_file = os.path.join(root_path, "config.json")
    file = open(config_file)

    return json.load(file)


@pytest.fixture(scope="function")
def login_page(page):
    return LoginPage(page)


@pytest.fixture(scope="function")
def api_client(config):
    api_url = config["web"]["api_url"]

    return Client(api_url)


@pytest.fixture(scope="function")
def created_object(api_client):
    """Создаем уникальный объект перед тестами GET, PUT, DELETE методов"""
    payload = {
        "name": f"{Faker().word().capitalize()} Phone {Faker().random_int(min=1, max=99)}",
        "data": {
            "year": Faker().year(),
            "price": Faker().pyfloat(left_digits=3, right_digits=2, positive=True, min_value=100, max_value=999),
            "CPU model": f'Chip-{Faker().lexify("???").upper()}'
        }
    }
    response = api_client.create_object(payload)
    assert response.status_code == HTTPStatus.OK

    object_data = response.json()
    yield object_data

    try:
        url = f'{api_client.base_url}/objects/{object_data["id"]}'
        requests.delete(url)
    except Exception:
        pass
