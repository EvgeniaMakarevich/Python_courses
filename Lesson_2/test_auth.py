from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data import USERNAME, PASSWORD, MAIN_PAGE, CATALOGUE_PAGE


# driver = webdriver.Chrome()

# @pytest.fixture(scope='function')
# def driver():
#     driver = webdriver.Chrome()  # Initialize WebDriver (Chrome example)
#     yield driver
#     driver.quit()


# @pytest.fixture(scope='function')
# def log_in():
#     driver.get('https://www.saucedemo.com/')
#     user_name_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
#     user_name_field.send_keys('standard_user')
#     time.sleep(1)
#     password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
#     password_field.send_keys('secret_sauce')
#
#     login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
#     login_button.click()
#     yield driver
#     driver.quit()


def test_login_form(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(USERNAME)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    time.sleep(5)
    assert driver.current_url == CATALOGUE_PAGE

