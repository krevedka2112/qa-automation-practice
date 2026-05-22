from http import HTTPStatus

from faker import Faker


def test_create_object(api_client):
    """Проверяем создание нового объекта"""
    object_name = f"{Faker().word().capitalize()} Phone {Faker().random_int(min=1, max=100)}"
    object_year = Faker().year()
    object_price = Faker().pyfloat(left_digits=3, right_digits=2, positive=True, min_value=100, max_value=999)
    payload = {
        "name": object_name,
        "data": {
            "year": object_year,
            "price": object_price,
        }
    }

    response = api_client.create_object(payload)
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert "id" in data and data["id"] is not None
    assert data["name"] == object_name
    assert data["data"]["year"] == object_year
    assert data["data"]["price"] == object_price
    assert "createdAt" in data


def test_get_object_by_id(api_client, created_object):
    """Проверяем получение объекта по id"""
    response = api_client.get_object(created_object["id"])
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert data["id"] == created_object["id"]
    assert data["name"] == created_object["name"]
    assert data["data"]["year"] == created_object["data"]["year"]
    assert data["data"]["price"] == created_object["data"]["price"]
    assert data["data"]["CPU model"] == created_object["data"]["CPU model"]


def test_update_object(api_client, created_object):
    """Проверяем обновление существующего объекта"""
    updated_name = f"Apple MacBook {Faker().word().capitalize()} {Faker().random_int(min=1, max=100)}"
    updated_price = Faker().pyfloat(left_digits=3, right_digits=2, positive=True, min_value=100, max_value=999)
    updated_year = Faker().year()
    updated_model = f"Apple M{Faker().random_int(min=1, max=9)} {Faker().word().capitalize()}"

    payload = {
        "name": updated_name,
        "data": {
            "year": updated_year,
            "price": updated_price,
            "CPU model": updated_model
        }
    }

    response = api_client.update_object(created_object["id"], payload)
    assert response.status_code == HTTPStatus.OK

    data = response.json()
    assert data["id"] == created_object["id"]
    assert data["name"] == updated_name
    assert data["data"]["price"] == updated_price
    assert data["data"]["year"] == updated_year
    assert data["data"]["CPU model"] == updated_model
    assert "updatedAt" in data


def test_delete_object(api_client, created_object):
    """Проверяем удаление объекта"""
    delete_response = api_client.delete_object(created_object["id"])
    assert delete_response.status_code == HTTPStatus.OK
    assert delete_response.json()["message"] == f'Object with id = {created_object["id"]} has been deleted.'

    get_resp = api_client.get_object(created_object["id"])
    assert get_resp.status_code == HTTPStatus.NOT_FOUND
