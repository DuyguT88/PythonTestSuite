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

  @visibility
  Scenario: Verify Visibility of Elements
    When I navigate to the Visibility page
    And I click the Hide button
    Then I verify the Removed button is not visible
    And I verify the Zero Width button is not visible
    And I verify the Overlapped button is not visible
    And I verify the Opacity 0 button is not visible
    And I verify the Visibility Hidden button is not visible
    And I verify the Display None button is not visible
    And I verify the Off Screen button is not visible