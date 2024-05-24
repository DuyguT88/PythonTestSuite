import requests
import random

BASE_URL = "https://petstore.swagger.io/v2"  # Base URL for the Petstore API


def generate_random_pet_id():
    return random.randint(10000, 99999)


def create_pet_data(pet_id=None, name="Rex", status="available"):
    if pet_id is None:
        pet_id = generate_random_pet_id()
    return {
        "id": pet_id,
        "name": name,
        "category": {"id": 1, "name": "Dogs"},
        "photoUrls": ["http://example.com/photo1"],
        "tags": [{"id": 1, "name": "Tag1"}],
        "status": status
    }


def send_post_request(endpoint, data):
    return requests.post(f"{BASE_URL}{endpoint}", json=data)


def send_put_request(endpoint, data):
    return requests.put(f"{BASE_URL}{endpoint}", json=data)


def send_delete_request(endpoint):
    return requests.delete(f"{BASE_URL}{endpoint}")


def validate_response_status(response, expected_status):
    assert response.status_code == expected_status, f"Expected status {expected_status}, got {response.status_code}"


def validate_response_contains(response, expected_data):
    response_json = response.json()
    for key, value in expected_data.items():
        assert response_json.get(key) == value, f"Expected {key} to be {value}, but got {response_json.get(key)}"
