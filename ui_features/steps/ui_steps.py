from behave import given, when, then
from selenium import webdriver
from ui_features.pages.text_input_page import TextInputPage
from ui_features.pages.dynamic_table_page import DynamicTablePage  # New import
from ui_features.pages.ajax_page import AjaxPage


@given('I open the browser')
def step_open_browser(context):
    context.driver = webdriver.Chrome()  # or use another WebDriver
    context.driver.maximize_window()


@when('I navigate to the Text Input page')
def step_navigate_text_input_page(context):
    context.page = TextInputPage(context.driver)
    context.page.navigate("http://www.uitestingplayground.com/textinput")


@when('I enter "{text}" into the text input')
def step_enter_text(context, text):
    context.page.enter_text(text)


@when('I click the button')
def step_click_button(context):
    context.page.click_button()


@then('I verify the button text is updated to "{expected_text}"')
def step_verify_button_text(context, expected_text):
    actual_text = context.page.get_button_text().strip()
    expected_text = expected_text.strip()
    assert actual_text == expected_text, f"Expected '{expected_text}', but got '{actual_text}'"


@when('I navigate to the Dynamic Table page')
def step_navigate_dynamic_table_page(context):
    context.page = DynamicTablePage(context.driver)
    context.page.navigate("http://www.uitestingplayground.com/dynamictable")


@then('I verify the Chrome CPU value matches the yellow label')
def step_verify_chrome_cpu_value(context):
    chrome_cpu = context.page.get_chrome_cpu_from_table()
    yellow_label_cpu = context.page.get_chrome_cpu_from_label()
    print(f"Chrome CPU value: {chrome_cpu}")
    print(f"Yellow label CPU value: {yellow_label_cpu}")
    assert chrome_cpu == yellow_label_cpu, f"Expected CPU value '{yellow_label_cpu}', but got '{chrome_cpu}'"


@when('I navigate to the AJAX page')
def step_navigate_ajax_page(context):
    context.page = AjaxPage(context.driver)
    context.page.navigate("http://www.uitestingplayground.com/ajax")


@when('I click the AJAX button')
def step_click_ajax_button(context):
    context.page.click_ajax_button()


@then('I verify content is loaded')
def step_verify_ajax_content(context):
    content = context.page.wait_for_content()
    assert content  # Add more detailed checks as needed


@then('I close the browser')
def step_close_browser(context):
    context.driver.quit()
