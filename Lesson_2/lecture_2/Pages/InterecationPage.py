from selenium.webdriver.common.by import By

from Python_courses.Lesson_2.lecture_2.Locators.Interaction_locators import Interactionslocators
from Python_courses.Lesson_2.lecture_2.Pages.base_page import Basepage
import time



class InteractionPage(Basepage):
    locators = Interactionslocators()

    def drop_simple(self):
        drop_div = self.element_is_visible(self.locators.DRAG)
        drag_div = self.element_is_visible(self.locators.DROP)
        self.drag_and_drop(drag_div, drop_div)
        text = self.element_is_visible(self.locators.DROP_TEXT).text
        time.sleep(10)
        assert text == 'Dropped!'


    def accept(self,driver):
        new_tab = driver.find_element(By.XPATH,'//*[@id="droppableExample-tab-accept"]')
        new_tab.click()
        acceptable = self.element_is_visible(self.locators.ACCEPT)
        not_acceptable = self.element_is_visible(self.locators.NOT_ACCEPT)
        drop = self.element_is_visible(self.locators.DROP_1)
        self.drag_and_drop(acceptable,drop)
        assert drop.value_of_css_property('.droppable-container .drop-box-outer.ui-active') == '#3cb371'
        self.drag_and_drop(not_acceptable, drop)
        assert drop.value_of_css_property('.droppable-container .ui-state-highlight') == '#4682b4'