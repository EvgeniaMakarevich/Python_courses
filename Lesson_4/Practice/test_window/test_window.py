from Python_courses.Lesson_4.Practice.pages.window import WindowPage
from Python_courses.Lesson_4.POM.conftest import driver,options
class Test_window:
    def test_new_tab(self,driver):
        page = WindowPage(driver,'https://demoqa.com/browser-windows')
        page.open()
        text = page.check_opened_new_tab()
        assert text == 'This is a sample page'


    def test_new_window(self,driver):
        page = WindowPage(driver, 'https://demoqa.com/browser-windows')
        page.open()
        text = page.check_opened_new_window()
        assert text == 'This is a sample page'