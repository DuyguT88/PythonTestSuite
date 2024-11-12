Feature: Swagger Petstore API operations

  Scenario: Adding a new pet
    Given I have the data for a new pet
    When I send a POST request to the "/pet" endpoint
    Then I receive a confirmation with status 200
    And I get that pet is created

  Scenario: Updating an existing pet
    Given a pet has been created
    And I have the data for an existing pet to update
    When I send a PUT request to the "/pet" endpoint
    Then I receive an updated confirmation with status 200
    And I get that the pet is updated

  Scenario: Deleting a pet
    Given a pet has been created
    And I have the pet ID to delete
    When I send a DELETE request to the "/pet/{petId}" endpoint
    Then I receive a deletion confirmation with status 200
    And I get that pet is deleted
