from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import pytest
from test_auth import log_in


# driver = webdriver.Chrome()


def test_add_to_cart(log_in):
    driver = log_in
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]'))
    )
    add_to_cart_button.click()

    remove_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]'))
    )
    assert remove_button.text == 'Remove'

    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert shopping_cart_badge.text == '1'

    item_name_before_cart = driver.find_element(By.CSS_SELECTOR, "a#item_4_title_link > div.inventory_item_name").text

    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]'))
    )
    cart_button.click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'

    item_name_in_cart = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text
    assert item_name_before_cart == item_name_in_cart


    product_name_in_cart = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="inventory_item_name"]'))
    )
    assert product_name_in_cart.is_displayed()
    assert product_name_in_cart.text == 'Sauce Labs Backpack'

    item_description = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="inventory_item_desc"]'))
    )
    assert item_description.is_displayed()
    assert item_description.text.startswith('carry.allTheThings() with')

    item_price = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]')
    assert item_price.text == '$29.99'

    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert shopping_cart_badge.text == '1'

def test_remove_from_cart(log_in):
    driver = log_in
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]'))
    )
    add_to_cart_button.click()

    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]'))
    )
    cart_button.click()

    remove_button_in_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]'))
    )
    remove_button_in_cart.click()

    try:
        driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]')
        assert False, "Remove button is still present after removing the item from the cart"
    except NoSuchElementException:
        assert True, "Remove button is not present after removing the item from the cart"

    try:
        driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]')
        assert False, "Item is still present in the cart after removal"
    except NoSuchElementException:
        assert True, "Item is not present in the cart after removal"

    continue_shopping_button = driver.find_element(By.XPATH, '//button[@data-test="continue-shopping"]')
    assert continue_shopping_button.is_displayed()

    checkout_button = driver.find_element(By.XPATH, '// button[@data-test="checkout"]')
    assert checkout_button.is_displayed()

    try:
        driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
        assert False, "Item is still present"
    except NoSuchElementException:
        assert True


def test_continue_shopping_with_product(log_in):
    driver = log_in
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]'))
    )
    add_to_cart_button.click()

    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert shopping_cart_badge.text == '1'

    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]'))
    )
    cart_button.click()

    continue_shopping_button = driver.find_element(By.XPATH, '//button[@data-test="continue-shopping"]')
    continue_shopping_button.click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert shopping_cart_badge.text == '1'


def test_continue_shopping_without_product(log_in):
    driver = log_in
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]'))
    )
    add_to_cart_button.click()

    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert shopping_cart_badge.text == '1'

    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]'))
    )
    cart_button.click()

    remove_button_in_cart = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]'))
    )
    remove_button_in_cart.click()

    try:
        driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
        assert False, "Item is still present"
    except NoSuchElementException:
        assert True

    continue_shopping_button = driver.find_element(By.XPATH, '//button[@data-test="continue-shopping"]')
    continue_shopping_button.click()
    assert driver.current_url == 'https://www.saucedemo.com/inventory.html'

    try:
        driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
        assert False, "Item is still present"
    except NoSuchElementException:
        assert True


def test_checkout_open(log_in):
    driver = log_in
    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]'))
    )
    add_to_cart_button.click()

    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]'))
    )
    cart_button.click()

    checkout_button = driver.find_element(By.XPATH, '// button[@data-test="checkout"]')
    checkout_button.click()
    assert driver.current_url == 'https://www.saucedemo.com/checkout-step-one.html'

    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert shopping_cart_badge.text == '1'





