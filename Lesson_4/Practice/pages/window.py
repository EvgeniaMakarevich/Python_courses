from Python_courses.Lesson_4.POM.base.selenium_base import BasePage
from Python_courses.Lesson_4.Practice.locators.locators_window import WindowPageLocators
import time

class WindowPage(BasePage):
    locators = WindowPageLocators()

    def check_opened_new_tab(self):
        self.is_clickable(self.locators.NEW_TAB).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.is_visible(self.locators.NEW_TAB_PAGE)
        self.driver.switch_to.window(self.driver.window_handles[0])
        time.sleep(3)
        return text.text

    def check_opened_new_window(self):
        self.is_clickable(self.locators.NEW_WINDOW).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        text = self.is_visible(self.locators.NEW_TAB_PAGE)
        time.sleep(3)
        return text.text