Feature: UI Testing Playground

  @text_input
  Scenario: Verify Text Input Functionality and Button Enablement
    Given I open the browser
    When I navigate to the Text Input page
    And I enter "Hello" into the text input
    And I click the button
    Then I verify the button text is updated to "Hello"
    And I close the browser

  @dynamic_table
  Scenario: Verify Dynamic Table CPU Value
    Given I open the browser
    When I navigate to the Dynamic Table page
    Then I verify the Chrome CPU value matches the yellow label
    And I close the browser

  @ajax_loading
  Scenario: Verify Asynchronous Content Loading with AJAX
    Given I open the browser
    When I navigate to the AJAX page
    And I click the AJAX button
    Then I verify content is loaded
    And I close the browser