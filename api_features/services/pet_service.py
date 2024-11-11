from .base_service import Base


class PetService(Base):
    def __init__(self, url, api_key):
        super().__init__(url, api_key)

    def create_pet_request(self, data):
        return self.send_post_request("/pet", data)

    def update_pet_request(self, data):
        return self.send_put_request("/pet", data)

    def retrieve_pet_request(self, pet_id):
        return self.send_get_request(f"/pet/{pet_id}")

    def delete_pet_request(self, pet_id):
        return self.send_delete_request(f"/pet/{pet_id}")

    @staticmethod
    def create_pet_data(id=None, category_id=1, category_name="Dogs", name="Buddy",
                        photo_urls=None, tags=None, status="available"):
        if photo_urls is None:
            photo_urls = ["https://example.com/photo"]
        if tags is None:
            tags = [{"id": 1, "name": "tag1"}]
        if id is None:
            id = PetService.generate_random_pet_id()

        return {
            "id": id,
            "category": {"id": category_id, "name": category_name},
            "name": name,
            "photoUrls": photo_urls,
            "tags": tags,
            "status": status
        }

    @staticmethod
    def generate_random_pet_id():
        import random
        return random.randint(100000, 999999)
