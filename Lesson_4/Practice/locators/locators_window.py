from selenium.webdriver.common.by import By


class WindowPageLocators:
    NEW_TAB = (By.XPATH, '//*[@id="tabButton"]')
    NEW_TAB_PAGE = (By.XPATH, '//*[@id="sampleHeading"]')
    NEW_WINDOW = (By.XPATH, '//*[@id="windowButton"]')
