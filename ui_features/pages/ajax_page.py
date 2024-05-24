from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from .base_page import BasePage


class AjaxPage(BasePage):
    AJAX_BUTTON = (By.ID, "ajaxButton")
    CONTENT = (By.ID, "content")

    def click_ajax_button(self):
        self.find_element(*self.AJAX_BUTTON).click()

    def wait_for_content(self):
        # Wait for the content element to contain some text
        WebDriverWait(self.driver, 20).until(
            EC.text_to_be_present_in_element(self.CONTENT, "loaded")
        )
        return self.wait_for_element(*self.CONTENT).text
