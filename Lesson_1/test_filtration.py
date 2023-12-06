from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pytest
from test_auth import log_in
import string
from selenium.webdriver.support.ui import Select


def test_filtration_az(log_in):
    driver = log_in

    try:
        sort_container = driver.find_element(By.XPATH, '//*[@data-test="product_sort_container"]')
        assert sort_container.is_displayed()
    except NoSuchElementException:
        assert False

    az_filtration = driver.find_element(By.XPATH, '//span[@class="active_option" and text()="Name (A to Z)"]')
    assert az_filtration.is_displayed()

    product_elements = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name "]')

    # Получение текста для каждого элемента и сохранение в списке
    product_titles = [x.text for x in product_elements]

    # Проверка, что полученные значения находятся в алфавитном порядке
    assert product_titles == sorted(product_titles)


def test_filtration_za(log_in):
    driver = log_in

    sort_dropdown = driver.find_element(By.XPATH, '//*[@data-test="product_sort_container"]')

    # Creating a Select object
    sort_dropdown_select = Select(sort_dropdown)

    # Selecting the second option (index 1 because index starts from 0)
    sort_dropdown_select.select_by_index(1)

    za_filtration = driver.find_element(By.XPATH, '//span[@class="active_option" and text()="Name (Z to A)"]')
    assert za_filtration.is_displayed()

    product_elements = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name "]')

    # Получение текста для каждого элемента и сохранение в списке
    product_titles = [x.text for x in product_elements]

    assert product_titles == sorted(product_titles, reverse=True)

def test_filtration_low_to_high(log_in):
    driver = log_in

    sort_dropdown = driver.find_element(By.XPATH, '//*[@data-test="product_sort_container"]')

    sort_dropdown_select = Select(sort_dropdown)

    # Select "Price (low to high)" from the dropdown using the text value
    sort_dropdown_select.select_by_visible_text("Price (low to high)")

    # Find the active filter to ensure Price (low to high) is displayed
    low_to_high_filter = driver.find_element(By.XPATH,
                                             '//span[@class="active_option" and text()="Price (low to high)"]')
    assert low_to_high_filter.is_displayed()

    # Get the list of product prices after the filter is applied
    product_price_class = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    product_prices = [parse_price(x.text) for x in product_price_class]

    # Check if the prices are sorted from low to high
    assert product_prices == sorted(product_prices)


# Helper function to convert the price string to a comparable format (e.g., float)
def parse_price(price_string):
    return float(price_string.replace('$', ''))

def test_filtration_high_to_low(log_in):
    driver = log_in
    sort_dropdown = driver.find_element(By.XPATH, '//*[@data-test="product_sort_container"]')
    sort_dropdown_select = Select(sort_dropdown)
    sort_dropdown_select.select_by_index(3)

    high_to_low_filter = driver.find_element(By.XPATH,
                                             '//span[@class="active_option" and text()="Price (high to low)"]')
    assert high_to_low_filter.is_displayed()

    product_price_class = driver.find_elements(By.XPATH, '//div[@class="inventory_item_price"]')
    product_prices = [parse_price(price.text) for price in product_price_class]

    assert product_prices == sorted(product_prices, reverse=True)

