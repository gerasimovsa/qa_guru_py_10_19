import requests
from jsonschema.validators import validate

from schemas.get_resource_schema import GET_RESOURCE_SCHEMA
from schemas.get_resources_list_schema import GET_RESOURCES_LIST_SCHEMA
from schemas.get_user_schema import GET_USER_SCHEMA
from schemas.get_users_list_schema import GET_USERS_LIST_SCHEMA

DOMAIN_URL = "https://reqres.in"
USERS_API = "/api/users/"
RESOURCES_API = "/api/resources/"


def test_get_users_list_schema_validation():
    response = requests.get(url=DOMAIN_URL + USERS_API)
    validate(response.json(), GET_USERS_LIST_SCHEMA)


def test_get_user_schema_validation():
    response = requests.get(url=DOMAIN_URL + USERS_API + "6")
    validate(response.json(), GET_USER_SCHEMA)


def test_get_resources_list_schema_validation():
    response = requests.get(url=DOMAIN_URL + RESOURCES_API)
    validate(response.json(), GET_RESOURCES_LIST_SCHEMA)


def test_get_resource_schema_validation():
    response = requests.get(url=DOMAIN_URL + RESOURCES_API + "6")
    validate(response.json(), GET_RESOURCE_SCHEMA)
