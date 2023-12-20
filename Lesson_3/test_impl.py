from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest
from selenium.webdriver.common.by import By


@pytest.fixture
def options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_visible_after_with_implicit(driver):
    driver.get('https://demoqa.com/dynamic-properties')
    button = driver.find_element(By.XPATH, "//button[@id ='visibleAfter']")
    assert button.is_displayed()