from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
from test_auth import log_in


def test_remove_product(log_in):
    driver = log_in
    add_to_cart_button_backpack = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]'))
    )
    add_to_cart_button_backpack.click()

    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert shopping_cart_badge.text == '1'

    add_to_cart_button_bike = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]'))
    )
    add_to_cart_button_bike.click()

    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert shopping_cart_badge.text == '2'

    remove_button_backpack = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]'))
    )
    remove_button_bike = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@data-test="remove-sauce-labs-bike-light"]'))
    )

    remove_button_backpack.click()
    remove_button_bike.click()

    try:
        driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
        assert True
    except NoSuchElementException:
        assert False

    try:
        driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-bike-light"]')
        assert True
    except NoSuchElementException:
        assert False

    try:
        driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
        assert False, "Item is still present"
    except NoSuchElementException:
        assert True

