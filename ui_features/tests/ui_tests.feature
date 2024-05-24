Feature: UI Testing Playground

  @text_input
  Scenario: Verify Text Input Functionality and Button Enablement
    When I navigate to the Text Input page
    And I enter "Hello" into the text input
    And I click the button
    Then I verify the button text is updated to "Hello"

  @dynamic_table
  Scenario: Verify Dynamic Table CPU Value
    When I navigate to the Dynamic Table page
    Then I verify the Chrome CPU value matches the yellow label

  @ajax_loading
  Scenario: Verify Asynchronous Content Loading with AJAX
    When I navigate to the AJAX page
    And I click the AJAX button
    Then I verify content is loaded