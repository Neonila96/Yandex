import requests

def test_geocoding_valid(base_url_geocod, api_key_geocod):
    params = {
        "apikey": api_key_geocod,
        "geocode": "Москва, Красная площадь",
        "format": "json"
    }
    response = requests.get(base_url_geocod, params=params)
    assert response.status_code == 200
    data = response.json()
    assert "GeoObject" in data["response"]["GeoObjectCollection"]["featureMember"][0]
def test_geocoding_invalid_key(base_url_geocod):
    params = {
        "apikey": "invalid_api_key",
        "geocode": "Москва, Красная площадь",
        "format": "json"
    }
    response = requests.get(base_url_geocod, params=params)
    assert response.status_code == 403
    assert "Invalid api key" in response.text
def test_organization_search_valid(base_url_org, api_key_org):
    params = {
        "apikey": api_key_org,
        "text": "кафе",
        "lang": "ru_RU",
        "ll": "37.6173,55.7558",  # Координаты центра Москвы
        "spn": "0.01,0.01",
        "type": "biz",
        "results": "5"
    }
    response = requests.get(base_url_org, params=params)
    assert response.status_code == 200
    data = response.json()
    assert len(data["features"]) > 0
def test_organization_search_empty(base_url_org, api_key_org):
    params = {
        "apikey": api_key_org,
        "text": "",
        "lang": "ru_RU",
        "ll": "37.6173,55.7558",
        "spn": "0.01,0.01",
        "type": "biz",
        "results": "5"
    }
    response = requests.get(base_url_org, params=params)
    assert response.status_code == 200
