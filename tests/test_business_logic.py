import requests
from data.resources import Resource

DOMAIN_URL = "https://reqres.in"
RESOURCES_API = "/api/resources/"


def test_create_resource():
    resource = Resource(name="test_resource", color="blue")
    payload = {"name": resource.name, "color": resource.color}
    response = requests.post(url=DOMAIN_URL + RESOURCES_API, data=payload)
    assert response.status_code == 201
    assert response.json()["name"] == resource.name
    assert response.json()["color"] == resource.color
    assert response.json()["id"] is not None
    assert response.json()["createdAt"] is not None


def test_create_resource_property():
    resource = Resource(id="6")
    payload = {"note": "Adding a note property to the resource entry"}
    response = requests.patch(url=DOMAIN_URL + RESOURCES_API + resource.id, data=payload)
    assert response.status_code == 200
    assert response.json()["note"] == "Adding a note property to the resource entry"


def test_delete_resource():
    resource = Resource(id="6")
    response = requests.delete(url=DOMAIN_URL + RESOURCES_API + resource.id)
    assert response.status_code == 204
    assert response.text == ""
