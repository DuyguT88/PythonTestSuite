from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from .base_page import BasePage


class TextInputPage(BasePage):
    TEXTBOX = (By.ID, "newButtonName")
    BUTTON = (By.ID, "updatingButton")
    BUTTON_TEXT = "Button That Should Change it's Name Based on Input Value"

    def enter_text(self, text):
        textbox = self.wait_for_element(*self.TEXTBOX)
        textbox.clear()
        textbox.send_keys(text)

    def click_button(self):
        # Locate the button by its text and click it
        button = self.wait_for_element(By.XPATH, f"//button[text()=\"{self.BUTTON_TEXT}\"]")
        button.click()

    def get_button_text(self):
        # Wait for the button text to be updated
        WebDriverWait(self.driver, 10).until(
            lambda driver: driver.find_element(*self.BUTTON).text != self.BUTTON_TEXT
        )
        button = self.find_element(*self.BUTTON)
        return button.text
