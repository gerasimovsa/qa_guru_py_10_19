import requests
from data.users import User

DOMAIN_URL = "https://reqres.in"
USERS_API = "/api/users/"
LOGIN_API = "/api/login/"


def test_get_user():
    user = User(id="6", first_name="Tracey", last_name="Ramos")
    response = requests.get(url=DOMAIN_URL + USERS_API + user.id)
    assert response.status_code == 200
    assert response.json()["data"]["first_name"] == user.first_name
    assert response.json()["data"]["last_name"] == user.last_name


def test_create_user():
    user = User(first_name="sergey", job="tester")
    payload = {"name": user.first_name, "job": user.job}
    response = requests.post(url=DOMAIN_URL + USERS_API, data=payload)
    assert response.status_code == 201
    assert response.json()["name"] == user.first_name
    assert response.json()["job"] == user.job
    assert response.json()["id"] is not None
    assert response.json()["createdAt"] is not None


def test_update_user():
    user = User(id="6", first_name="sergey", job="tester")
    payload = {"name": user.first_name, "job": user.job}
    response = requests.put(url=DOMAIN_URL + USERS_API + user.id, data=payload)
    assert response.status_code == 200
    assert response.json()["name"] == user.first_name
    assert response.json()["job"] == user.job
    assert response.json()["updatedAt"] is not None


def test_get_invalid_user():
    response = requests.get(url=DOMAIN_URL + USERS_API + "16")
    assert response.status_code == 404
    assert response.json() == {}


def test_login_unsuccessful():
    user = User(email="sergey@reqres.in", password="test_password")
    payload = {"email": user.email, "password": user.password}
    response = requests.post(url=DOMAIN_URL + LOGIN_API, data=payload)
    assert response.status_code == 400
    assert response.json()["error"] == "user not found"
