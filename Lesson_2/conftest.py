from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON
from data import USERNAME, PASSWORD, MAIN_PAGE, CATALOGUE_PAGE
from locators import add_to_cart_button_backpack,shopping_cart_link, checkout_button
from data import CART_PAGE, title_backpack, description_text, remove_button_text, price_backpack



@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture(scope='function')
def log_in(driver):
    driver.get('https://www.saucedemo.com/')
    user_name_field = driver.find_element(By.XPATH, USERNAME_FIELD)
    user_name_field.send_keys(USERNAME)

    password_field = driver.find_element(By.XPATH, PASSWORD_FIELD)
    password_field.send_keys(PASSWORD)

    login_button = driver.find_element(By.XPATH, LOGIN_BUTTON)
    login_button.click()
    yield driver

@pytest.fixture(scope='function')
def add_to_cart(log_in):
    driver = log_in  # Ensure to capture the 'driver' instance returned by 'log_in'
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_to_cart_button_backpack))
    ).click()
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, shopping_cart_link))
    ).click()
    yield driver


@pytest.fixture(scope='function')
def add_to_checkout(add_to_cart):
    driver = add_to_cart
    driver.find_element(By.XPATH, checkout_button).click()
    yield driver
