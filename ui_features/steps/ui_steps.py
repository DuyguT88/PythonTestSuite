from behave import given, when, then
from ui_features.pages.text_input_page import TextInputPage
from ui_features.pages.dynamic_table_page import DynamicTablePage
from ui_features.pages.ajax_page import AjaxPage
from ui_features.pages.visibility_page import VisibilityPage


@when('I navigate to the Text Input page')
def step_navigate_text_input_page(context):
    context.page = TextInputPage(context.driver)
    context.page.navigate(f"{context.base_url}/textinput")


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
    context.page.navigate(f"{context.base_url}/dynamictable")


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
    context.page.navigate(f"{context.base_url}/ajax")


@when('I click the AJAX button')
def step_click_ajax_button(context):
    context.page.click_ajax_button()


@then('I verify content is loaded')
def step_verify_ajax_content(context):
    content = context.page.wait_for_content()
    assert content  # Add more detailed checks as needed


@when('I navigate to the Visibility page')
def step_navigate_visibility_page(context):
    context.page = VisibilityPage(context.driver)
    context.page.navigate(f"{context.base_url}/visibility")


@when('I click the Hide button')
def step_click_hide_button(context):
    context.page.click_hide_button()


@then('I verify the Removed button is not visible')
def step_verify_removed_button_not_visible(context):
    assert not context.page.is_removed_button_visible(), "Removed button is visible"


@then('I verify the Zero Width button is not visible')
def step_verify_zero_width_button_not_visible(context):
    assert not context.page.is_zero_width_button_visible(), "Zero Width button is visible"


@then('I verify the Overlapped button is not visible')
def step_verify_overlapped_button_not_visible(context):
    assert not context.page.is_overlapped_button_visible(), "Overlapped button is visible"


@then('I verify the Opacity 0 button is not visible')
def step_verify_opacity_0_button_not_visible(context):
    assert not context.page.is_opacity_0_button_visible(), "Opacity 0 button is visible"


@then('I verify the Visibility Hidden button is not visible')
def step_verify_visibility_hidden_button_not_visible(context):
    assert not context.page.is_visibility_hidden_button_visible(), "Visibility Hidden button is visible"


@then('I verify the Display None button is not visible')
def step_verify_display_none_button_not_visible(context):
    assert not context.page.is_display_none_button_visible(), "Display None button is visible"


@then('I verify the Off Screen button is not visible')
def step_verify_off_screen_button_not_visible(context):
    assert not context.page.is_off_screen_button_visible(), "Off Screen button is visible"
