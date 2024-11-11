import requests


class Base:
    def __init__(self, base_url, api_key):
        self.base_url = base_url
        self.api_key = api_key

    def send_post_request(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        response = requests.post(url, json=data)
        return response

    def send_put_request(self, endpoint, data):
        url = f"{self.base_url}{endpoint}"
        response = requests.put(url, json=data)
        return response

    def send_delete_request(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        headers = {"Authorization": f"Bearer {self.api_key}"} if self.api_key else {}
        response = requests.delete(url, headers=headers)
        return response

    def send_get_request(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = requests.get(url)
        return response

    @staticmethod
    def validate_response_status(response, expected_status):
        assert response.status_code == expected_status, f"Expected status {expected_status}, but got {response.status_code}"

    @staticmethod
    def validate_response_contains(response, expected_data):
        response_data = response.json()
        for key, value in expected_data.items():
            assert response_data.get(key) == value, f"Expected {key} to be {value}, but got {response_data.get(key)}"
