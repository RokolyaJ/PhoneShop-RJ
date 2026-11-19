import requests

BASE_URL = "http://localhost:5000"


def test_home():
    response = requests.get(f"{BASE_URL}/")
    assert response.status_code == 200


def test_get_phones():
    response = requests.get(f"{BASE_URL}/phones")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
