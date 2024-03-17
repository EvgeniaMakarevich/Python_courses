from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pytest

@pytest.fixture
def options():
    options = Options()
    options.add_argument('--window-size=500,500')
    options.add_argument('--incognito')
    # options.add_argument('--headless')
    return options

@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()
def test_example(driver):
    driver.get('https://www.saucedemo.com/')
    assert driver.current_url == 'https://www.saucedemo.com/'


