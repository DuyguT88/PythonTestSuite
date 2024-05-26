from behave import given, when, then
from api_features.utils import create_pet_data, send_post_request, send_put_request, send_delete_request, \
    validate_response_status, validate_response_contains, send_get_request


@given('I have the data for a new pet')
def step_given_new_pet_data(context):
    context.new_pet_data = create_pet_data()


@given('a pet has been created')
def step_given_pet_created(context):
    context.pet_data = create_pet_data()
    response = send_post_request("/pet", context.pet_data)
    validate_response_status(response, 200)


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
    response = send_post_request("/pet", context.new_pet_data)
    context.response = response
    context.expected_data = context.new_pet_data


@when('I send a PUT request to the "/pet" endpoint')
def step_when_send_put_request(context):
    response = send_put_request("/pet", context.updated_pet_data)
    context.response = response
    context.expected_data = context.updated_pet_data


@when('I send a DELETE request to the "/pet/{petId}" endpoint')
def step_when_send_delete_request(context, petId):
    response = send_delete_request(f"/pet/{context.pet_id}")
    context.response = response
    context.expected_data = {"code": 200, "type": "unknown", "message": str(context.pet_id)}


@then('I receive a confirmation with status 200')
@then('I receive an updated confirmation with status 200')
@then('I receive a deletion confirmation with status 200')
def step_then_receive_confirmation(context):
    validate_response_status(context.response, 200)
    validate_response_contains(context.response, context.expected_data)


@then('I get that pet is created')
def step_then_get_pet_created(context):
    response = send_get_request(f"/pet/{context.expected_data['id']}")
    validate_response_status(response, 200)
    validate_response_contains(response, context.expected_data)


@then('I get that the pet is updated')
def step_then_get_pet_updated(context):
    response = send_get_request(f"/pet/{context.expected_data['id']}")
    validate_response_status(response, 200)
    validate_response_contains(response, context.expected_data)


@then('I get that pet is deleted')
def step_then_get_pet_deleted(context):
    response = send_get_request(f"/pet/{context.pet_id}")
    validate_response_status(response, 404)  # Assuming the API returns 404 for deleted pets
