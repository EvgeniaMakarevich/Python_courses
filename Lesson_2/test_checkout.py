
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from conftest import log_in
import time
from locators import (checkout_button,checkout_title,continue_button,cancel_button,first_name_input,last_name_input,zip_input,
                      text_error, svg_cross, error_fields,error_message_container, error_button,error_message_anscestor,item_name_backpack,
                      description_backpack,price_backpack_loc,item_total,item_full_total,taxes)
from data import (checkout_title_text,CHECKOUT_1,first_name_error_text,svg_cross_color,font_size,place_holder_fn,place_holder_ln,place_holder_zip
                  ,background,last_name_error_text,zip_name_error_text)

fake = Faker()

def test_checkout_interface(log_in,add_to_cart):
    driver = add_to_cart
    driver.find_element(By.XPATH, checkout_button).click()
    assert driver.find_element(By.XPATH, checkout_title).is_displayed()
    assert driver.find_element(By.XPATH, checkout_title).text == checkout_title_text
    assert driver.find_element(By.XPATH, continue_button).is_displayed()
    assert driver.find_element(By.XPATH, cancel_button).is_displayed()

    assert driver.find_element(By.XPATH, first_name_input).is_displayed()
    assert driver.find_element(By.XPATH, first_name_input).is_enabled()

    assert driver.find_element(By.XPATH, last_name_input).is_displayed()
    assert driver.find_element(By.XPATH, last_name_input).is_enabled()

    assert driver.find_element(By.XPATH, zip_input).is_displayed()
    assert driver.find_element(By.XPATH, zip_input).is_enabled()



def test_empty_fields(log_in,add_to_cart):
    driver = add_to_cart
    driver.find_element(By.XPATH, checkout_button).click()

    try:
        driver.find_element(By.XPATH, continue_button).click()
    except NoSuchElementException:
        pass

    assert driver.current_url == CHECKOUT_1
    assert driver.find_element(By.XPATH,error_message_container).is_displayed()
    assert driver.find_element(By.XPATH,text_error).text == first_name_error_text


    error_crosses = driver.find_elements(By.CSS_SELECTOR,svg_cross)
    for x in error_crosses:
        assert x.is_displayed()
        assert x.value_of_css_property('color') == svg_cross_color
        assert x.value_of_css_property('font-size') == font_size
        assert x.value_of_css_property('position') == 'absolute'
        assert x.value_of_css_property('right') == '0px'
        assert x.value_of_css_property('top') == '12px'

        input_element = x.find_element(By.XPATH, './preceding-sibling::input')
        assert input_element.is_displayed()

    assert len(error_crosses) == 3

    input_error_fields = driver.find_elements(By.XPATH, error_fields)
    for x in input_error_fields:
        assert x.value_of_css_property('border-bottom-color') == svg_cross_color
        assert x.value_of_css_property('padding') == '10px 0px'
        assert x.value_of_css_property('border') == ''
        assert x.value_of_css_property('width') == '380px'
        assert x.value_of_css_property('font-size') == '14px'
        assert x.value_of_css_property('font-family') == '"DM Sans", Arial, Helvetica, sans-serif'


    assert input_error_fields[0].get_attribute('placeholder') == place_holder_fn
    assert input_error_fields[1].get_attribute('placeholder') == place_holder_ln
    assert input_error_fields[2].get_attribute('placeholder') == place_holder_zip


    assert driver.find_element(By.XPATH, error_message_container).value_of_css_property('background-color') == svg_cross_color
    assert driver.find_element(By.XPATH, error_button).is_enabled()

    error_button_item = driver.find_element(By.XPATH, error_button)
    error_message_container_item = driver.find_element(By.XPATH, error_message_container)

    assert error_button_item.find_element(By.XPATH,
                                          error_message_anscestor) is not None

    error_button_item.click()

    for x in input_error_fields:
        assert x.value_of_css_property('background') == background




def test_empty_last_zip(add_to_checkout):
    driver = add_to_checkout
    driver.find_element(By.XPATH, first_name_input).send_keys(fake.name())
    driver.find_element(By.XPATH, continue_button).click()
    assert driver.find_element(By.XPATH, error_message_container).is_displayed()
    assert driver.find_element(By.XPATH, text_error).text == last_name_error_text


def test_empty_zip(add_to_checkout):
    driver = add_to_checkout
    driver.find_element(By.XPATH, first_name_input).send_keys(fake.name())
    driver.find_element(By.XPATH, last_name_input).send_keys(fake.name())
    driver.find_element(By.XPATH, continue_button).click()
    assert driver.find_element(By.XPATH, error_message_container).is_displayed()
    assert driver.find_element(By.XPATH, text_error).text == zip_name_error_text


def test_checkout_item(add_to_cart):
    driver = add_to_cart
    item_name_cart = driver.find_element(By.XPATH, item_name_backpack).text
    item_description_cart = driver.find_element(By.XPATH, description_backpack).text
    item_price_cart = driver.find_element(By.XPATH,price_backpack_loc).text


    checkout_button_link = WebDriverWait(driver,30).until(EC.element_to_be_clickable((By.XPATH, checkout_button)))
    checkout_button_link.click()
    driver.find_element(By.XPATH, first_name_input).send_keys(fake.name())
    driver.find_element(By.XPATH, last_name_input).send_keys(fake.name())
    driver.find_element(By.XPATH, zip_input).send_keys(fake.text())
    continue_element = WebDriverWait(driver,10).until(EC.element_to_be_clickable((By.XPATH, continue_button)))
    continue_element.click()

    expected_url = 'https://www.saucedemo.com/checkout-step-two.html'
    assert WebDriverWait(driver, 10).until(EC.url_contains(expected_url))

    assert item_price_cart == driver.find_element(By.XPATH,price_backpack_loc).text
    assert item_description_cart == driver.find_element(By.XPATH,description_backpack).text
    assert item_name_cart == driver.find_element(By.XPATH,item_name_backpack).text
    item_total_text = driver.find_element(By.XPATH, item_total).text
    assert item_price_cart in item_total_text


    taxes_label = driver.find_element(By.XPATH,taxes).text
    full_total = driver.find_element(By.XPATH,item_full_total).text

    subtotal_arr = item_total_text.split('$')
    tax_arr = taxes_label.split('$')
    total_arr = full_total.split('$')

    sub_total_amount = float(subtotal_arr[1])
    taxes_amount = float(tax_arr[1])
    total_amount = float(total_arr[1])

    assert taxes_amount + sub_total_amount == total_amount














