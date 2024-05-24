from selenium.webdriver.common.by import By
import re
from .base_page import BasePage


class DynamicTablePage(BasePage):
    dynamic_table_selector = (By.XPATH, "//div[@role='row']//span[text()='Chrome']")
    chrome_cpu_label_selector = (By.XPATH, "//p[contains(text(), 'Chrome CPU:')]")

    def get_chrome_cpu_from_table(self):
        print("Waiting for Chrome row in table to be visible...")
        chrome_row = self.wait_for_element(*self.dynamic_table_selector)
        print("Found Chrome row in table")
        # Find the CPU usage cell adjacent to the Chrome row
        cpu_usage_cell = chrome_row.find_element(By.XPATH, "following-sibling::*[contains(text(), '%')]")
        # Return the text content of the CPU usage cell
        return cpu_usage_cell.text

    def get_chrome_cpu_from_label(self):
        print("Waiting for Yellow Label to be visible...")
        chrome_cpu_text = self.wait_for_element(*self.chrome_cpu_label_selector).text
        print("Found Yellow Label")
        cpu_usage_match = re.search(r"(\d+(\.\d+)?)%", chrome_cpu_text)  # Regex to find numeric value
        return cpu_usage_match.group(0) if cpu_usage_match else None
