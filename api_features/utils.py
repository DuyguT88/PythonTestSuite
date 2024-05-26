import requests

BASE_URL = "https://petstore.swagger.io/v2"


def create_pet_data():
    return {
        "id": generate_random_pet_id(),
        "category": {"id": 1, "name": "Dogs"},
        "name": "Buddy",
        "photoUrls": ["https://example.com/photo"],
        "tags": [{"id": 1, "name": "tag1"}],
        "status": "available"
    }


def generate_random_pet_id():
    import random
    return random.randint(100000, 999999)


def send_post_request(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    response = requests.post(url, json=data)
    return response


def send_put_request(endpoint, data):
    url = f"{BASE_URL}{endpoint}"
    response = requests.put(url, json=data)
    return response


def send_delete_request(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.delete(url)
    return response


def send_get_request(endpoint):
    url = f"{BASE_URL}{endpoint}"
    response = requests.get(url)
    return response


def validate_response_status(response, expected_status):
    assert response.status_code == expected_status, f"Expected status {expected_status}, but got {response.status_code}"


def validate_response_contains(response, expected_data):
    response_data = response.json()
    for key, value in expected_data.items():
        assert response_data.get(key) == value, f"Expected {key} to be {value}, but got {response_data.get(key)}"
