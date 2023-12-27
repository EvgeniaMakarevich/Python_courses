from selenium.webdriver.common.by import By


class FrameLocators():
    FRAME_PAGE = (By.XPATH, '//*[@id="sampleHeading"]')

    FRAME = {
        'big': (By.XPATH, '//*[@id="frame1"]'),
        'small': (By.XPATH, '//*[@id="frame2"]')
    }
