import pytest
import requests

@pytest.fixture(scope="module")
def base_url_geocod():
    base_url_geocod = "https://geocode-maps.yandex.ru/1.x/"
    return base_url_geocod

@pytest.fixture(scope="module")
def base_url_org():
    base_url_org = "https://search-maps.yandex.ru/v1/"
    return base_url_org

@pytest.fixture(scope="module")
def api_key_geocod():
    api_key_geocod = "9377a4a4-a46c-4a2b-acd8-6d91cda968b1"
    return api_key_geocod

@pytest.fixture(scope="module")
def api_key_org():
    api_key_org = "44985ea4-05d0-4ce1-9b32-1aa3372508f1"
    return api_key_org


#setup
@pytest.fixture(scope="module", autouse=True)
def setup(base_url_geocod, api_key_geocod):
    # запрос по адресу
    query_params_geocod = {
        "apikey": api_key_geocod,
        "geocode": "Москва, Красная площадь",
        "format": "json"
    }

    response = requests.get(base_url_geocod, params=query_params_geocod)
    print(response.status_code)
    print("Поиск по геокоду" + response.text)
    assert response.status_code == 200
