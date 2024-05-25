from selenium.webdriver.common.by import By
from .base_page import BasePage

class VisibilityPage(BasePage):
    HIDE_BUTTON = (By.ID, "hideButton")
    REMOVED_BUTTON = (By.ID, "removedButton")
    ZERO_WIDTH_BUTTON = (By.ID, "zeroWidthButton")
    OVERLAPPED_BUTTON = (By.ID, "overlappedButton")
    OPACITY_0_BUTTON = (By.ID, "opacityZeroButton")
    VISIBILITY_HIDDEN_BUTTON = (By.ID, "visibilityHiddenButton")
    DISPLAY_NONE_BUTTON = (By.ID, "displayNoneButton")
    OFF_SCREEN_BUTTON = (By.ID, "offscreenButton")

    def click_hide_button(self):
        self.find_element(*self.HIDE_BUTTON).click()

    def is_removed_button_visible(self):
        return self.is_element_visible(*self.REMOVED_BUTTON)

    def is_zero_width_button_visible(self):
        return self.is_element_visible(*self.ZERO_WIDTH_BUTTON)

    def is_overlapped_button_visible(self):
        return self.is_element_visible(*self.OVERLAPPED_BUTTON) and not self.is_element_overlapped(*self.OVERLAPPED_BUTTON)

    def is_opacity_0_button_visible(self):
        return self.is_element_visible(*self.OPACITY_0_BUTTON)

    def is_visibility_hidden_button_visible(self):
        return self.is_element_visible(*self.VISIBILITY_HIDDEN_BUTTON)

    def is_display_none_button_visible(self):
        return self.is_element_visible(*self.DISPLAY_NONE_BUTTON)

    def is_off_screen_button_visible(self):
        return self.is_element_visible(*self.OFF_SCREEN_BUTTON)

    def is_element_overlapped(self, *locator):
        element = self.find_element(*locator)
        return self.driver.execute_script("""
            var elem = arguments[0], box = elem.getBoundingClientRect(), cx = box.left + box.width / 2, cy = box.top + box.height / 2,
                e = document.elementFromPoint(cx, cy); 
            for (; e; e = e.parentElement) {
                if (e === elem)
                    return false;
            }
            return true;
            """, element)
