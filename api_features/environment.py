import os
from api_features.services.pet_service import PetService


def before_all(context):
    context.BASE_URL = "https://petstore.swagger.io/v2"
    context.API_KEY = os.getenv("PETSTORE_API_TOKEN", "test123*")
    context.pet_service = PetService(context.BASE_URL, context.API_KEY)


def before_scenario(context, scenario):
    context.pet_id = None
    context.response = None
    context.pet_data = None
    context.new_pet_data = None
    context.updated_pet_data = None


def after_scenario(context, scenario):
    context.pet_service.delete_pet_if_exists(context.pet_id)
