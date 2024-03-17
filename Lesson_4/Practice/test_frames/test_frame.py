from Python_courses.Lesson_4.Practice.pages.frame_page import PageFrame
from Python_courses.Lesson_4.POM.conftest import driver,options
import pytest
class TestFrame:


        @pytest.mark.parametrize('size', ['big', 'small'])
        def test_frame(self, driver, size):
            page = PageFrame(driver, 'https://demoqa.com/frames')
            page.open()
            data = page.get_frame_size(size=size)
            width, height, text = page.frame(size=size)
            assert width == data['width'] and height == data['height']
            assert text == 'This is a sample page'

