from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver


def test_sign_up(driver):
    driver.get = 'https://the-internet.herokuapp.com/basic_auth'
    alert = driver.switch_to.alert
    alert.accept()