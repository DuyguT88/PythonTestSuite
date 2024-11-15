from behave import given, when, then
#from api_features.config.config import BASE_URL, API_KEY
#from api_features.services.pet_service import PetService



@given('I have the data for a new pet')
def step_given_new_pet_data(context):
    context.new_pet_data = context.pet_service.create_pet_data()


@given('a pet has been created')
def step_given_pet_created(context):
    context.pet_data = context.pet_service.create_pet_data()
    response = context.pet_service.create_pet_request(context.pet_data)
    context.pet_service.validate_response_status(response, 200)

    # Save the pet ID for deletion
    context.pet_id = context.pet_data['id']

    # Verify the pet exists by retrieving it
    response = context.pet_service.retrieve_pet_request(context.pet_id)
    context.pet_service.validate_response_status(response, 200)


@given('I have the data for an existing pet to update')
def step_given_existing_pet_data(context):
    context.updated_pet_data = context.pet_data.copy()
    context.updated_pet_data["name"] = "Rex Updated"
    context.updated_pet_data["status"] = "sold"


@given('I have the pet ID to delete')
def step_given_pet_id(context):
    context.pet_id = context.pet_data["id"]


@when('I send a POST request to the "/pet" endpoint')
def step_when_send_post_request(context):
    response = context.pet_service.create_pet_request(context.new_pet_data)
    context.response = response
    context.expected_data = context.new_pet_data


@when('I send a PUT request to the "/pet" endpoint')
def step_when_send_put_request(context):
    response = context.pet_service.update_pet_request(context.updated_pet_data)
    context.response = response
    context.expected_data = context.updated_pet_data


@when('I send a DELETE request to the "/pet/{petId}" endpoint')
def step_when_send_delete_request(context, petId):
    response = context.pet_service.delete_pet_request(f"{context.pet_id}")
    context.response = response
    context.expected_data = {"code": 200, "type": "unknown", "message": str(context.pet_id)}


@then('I receive a confirmation with status 200')
@then('I receive an updated confirmation with status 200')
@then('I receive a deletion confirmation with status 200')
def step_then_receive_confirmation(context):
    context.pet_service.validate_response_status(context.response, 200)
    context.pet_service.validate_response_contains(context.response, context.expected_data)


@then('I get that pet is created')
def step_then_get_pet_created(context):
    # Access the 'id' from the 'new_pet_data' dictionary correctly
    pet_id = context.new_pet_data['id']
    response = context.pet_service.retrieve_pet_request(pet_id)

    # Validate the response status and content
    context.pet_service.validate_response_status(response, 200)
    context.pet_service.validate_response_contains(response, context.new_pet_data)


@then('I get that the pet is updated')
def step_then_get_pet_updated(context):
    # Access the 'id' from the 'new_pet_data' dictionary correctly
    pet_id = context.expected_data['id']
    response = context.pet_service.retrieve_pet_request(pet_id)

    # Validate the response status and content
    context.pet_service.validate_response_status(response, 200)
    context.pet_service.validate_response_contains(response, context.expected_data)


@then('I get that pet is deleted')
def step_then_get_pet_deleted(context):
    response = context.pet_service.retrieve_pet_request(context.pet_id)
    context.pet_service.validate_response_status(response, 404)  # Assuming the API returns 404 for deleted pets
