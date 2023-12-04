from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_login_form():
    driver.get('https://www.saucedemo.com/')
    time.sleep(1)
    user_name_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    user_name_field.send_keys('standard_user')

    time.sleep(1)

    password_field = driver.find_element(By.XPATH,'//input[@data-test="password"]')
    password_field.send_keys('secret_sauce')

    time.sleep(1)

    login_button = driver.find_element(By.XPATH,'//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(5)
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    driver.quit()