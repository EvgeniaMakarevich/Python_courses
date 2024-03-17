from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time

import pytest
from test_auth import log_in

def test_logout(log_in):
    driver = log_in
    burger_menu_button = driver.find_element(By.XPATH, "//button[@id = 'react-burger-menu-btn']")
    burger_menu_button.click()
    logout_link = WebDriverWait(driver, timeout=10).until(EC.element_to_be_clickable(driver.find_element(By.XPATH,"//a[@id = 'logout_sidebar_link']")))
    logout_link.click()
    assert driver.current_url == 'https://www.saucedemo.com/'
