from Python_courses.Lesson_4.POM.base.selenium_base import BasePage
from Python_courses.Lesson_4.Practice.locators.locators_frame import FrameLocators

class PageFrame(BasePage):

    locators = FrameLocators()

    def frame(self,size):
        locator = self.locators.FRAME[size]
        frame = self.driver.find_element(*locator)
        width = frame.get_attribute('width')
        height = frame.get_attribute('height')
        self.driver.switch_to.frame(frame)
        text = self.is_visible(self.locators.FRAME_PAGE).text
        return width, height, text

    def get_frame_size(self, size):
        data = {
            'big': {
                'width': '500px',
                'height': '350px'
            },
            'small': {
                'width': '100px',
                'height': '100px'
            }
        }
        return data[size]



