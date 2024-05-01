import requests
from data.users import User

DOMAIN_URL = "https://reqres.in"
REGISTER_API = "/api/register/"


def test_register_successful():
    user = User(email="tracey.ramos@reqres.in", password="test_password")
    payload = {"email": user.email, "password": user.password}
    response = requests.post(url=DOMAIN_URL + REGISTER_API, data=payload)
    assert response.status_code == 200
    assert response.json()["id"] == 6
    assert response.json()["token"] is not None


def test_register_invalid_email():
    user = User(email="sergey@reqres.in", password="test_password")
    payload = {"email": user.email, "password": user.password}
    response = requests.post(url=DOMAIN_URL + REGISTER_API, data=payload)
    assert response.status_code == 400
    assert response.json()["error"] == "Note: Only defined users succeed registration"


def test_register_no_email():
    user = User(password="test_password")
    payload = {"password": user.password}
    response = requests.post(url=DOMAIN_URL + REGISTER_API, data=payload)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing email or username"


def test_register_no_password():
    user = User(email="sergey@reqres.in")
    payload = {"email": user.email}
    response = requests.post(url=DOMAIN_URL + REGISTER_API, data=payload)
    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"
