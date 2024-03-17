
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from conftest import log_in
from locators import add_to_cart_button_backpack, remove_button_backpack, shopping_cart_badge_1,item_name_before_cart_backpack, shopping_cart_link,description_backpack,price_backpack_loc
from data import CART_PAGE, title_backpack, description_text, remove_button_text, price_backpack



def test_add_to_cart(log_in):
    driver = log_in

    assert WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_to_cart_button_backpack))
    ).is_enabled()

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, add_to_cart_button_backpack))
    ).click()

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, remove_button_backpack))
    ).text == remove_button_text
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, remove_button_backpack))
    ).is_enabled()


    assert driver.find_element(By.XPATH, shopping_cart_badge_1).text == '1'

    item_name_before_cart = driver.find_element(By.CSS_SELECTOR, item_name_before_cart_backpack).text

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, shopping_cart_link))
    ).click()
    assert driver.current_url == CART_PAGE


    assert item_name_before_cart == driver.find_element(By.CSS_SELECTOR, item_name_before_cart_backpack).text

    assert driver.find_element(By.CSS_SELECTOR, item_name_before_cart_backpack).text == title_backpack


    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, description_backpack))
    ).is_displayed()
    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, description_backpack))
    ).text.startswith(description_text)

    assert driver.find_element(By.XPATH, price_backpack_loc).text == price_backpack

    assert driver.find_element(By.XPATH, shopping_cart_badge_1).text == '1'

    assert WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, remove_button_backpack))
    ).is_enabled()

def test_remove_from_cart(log_in,add_to_cart):
    driver = log_in

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





