from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from test_auth import log_in
import pytest
def test_product_card(log_in):
    driver = log_in
    product_item_text = driver.find_element(By.XPATH,"//a[@id ='item_4_title_link']/div[@class ='inventory_item_name ']").text
    product_item = driver.find_element(By.XPATH,
                                            "//a[@id ='item_4_title_link']/div[@class ='inventory_item_name ']")
    item_description = driver.find_element(By.XPATH, "//*[@id='inventory_container']/div/div[1]/div[2]/div[1]/div").text
    item_price = driver.find_element(By.XPATH, "//div[@class='inventory_item_label']/a[@id='item_4_title_link']/following::div[@class='inventory_item_price'][1]").text
    item_image = driver.find_element(By.XPATH, '//*[@id="item_4_img_link"]/img').get_attribute('src')


    product_item.click()
    assert driver.current_url == "https://www.saucedemo.com/inventory-item.html?id=4"

    product_title_card = driver.find_element(By.XPATH,"//div[@class = 'inventory_details_name large_size']")
    assert product_item_text == product_title_card.text


    add_to_cart_button = driver.find_element(By.XPATH,'//*[@id="add-to-cart-sauce-labs-backpack"]')
    assert add_to_cart_button.is_displayed()

    product_image_card = driver.find_element(By.XPATH,"//img[@class='inventory_details_img']")
    assert product_image_card.is_displayed()

    item_description_card = driver.find_element(By.XPATH,"//div[@class = 'inventory_details_desc large_size']")
    assert item_description == item_description_card.text


    item_price_card =driver.find_element(By.XPATH,"//div[@class='inventory_details_price']")
    assert item_price == item_price_card.text

    item_image_card = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]//img')
    assert item_image == item_image_card.get_attribute('src')




def test_add_to_card_product(log_in):
    driver = log_in
    product_item = driver.find_element(By.XPATH,
                                       "//a[@id ='item_4_title_link']/div[@class ='inventory_item_name ']")

    product_item.click()
    add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_button.click()

    remove_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]'))
    )

    assert remove_button.is_displayed()

    try:
        add_to_cart_button = driver.find_element(By.XPATH, '//*[@id="add-to-cart-sauce-labs-backpack"]')
        assert False
    except NoSuchElementException:
        assert True

    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    assert shopping_cart_badge.text == '1'

    product_title_card = driver.find_element(By.XPATH, "//div[@class = 'inventory_details_name large_size']").text
    item_description_card = driver.find_element(By.XPATH, "//div[@class = 'inventory_details_desc large_size']").text

    item_price_card = driver.find_element(By.XPATH, "//div[@class='inventory_details_price']").text

    # item_image_card = driver.find_element(By.XPATH, '//*[@id="inventory_item_container"]//img').get_attribute('src')

    cart_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, '//a[@class="shopping_cart_link"]'))
    )
    cart_button.click()
    assert driver.current_url == 'https://www.saucedemo.com/cart.html'

    item_name_in_cart = driver.find_element(By.XPATH, '//div[@class="inventory_item_name"]').text
    item_description_cart = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, '//div[@class="inventory_item_desc"]'))
    ).text
    item_price_cart = driver.find_element(By.XPATH, '//div[@class="inventory_item_price"]').text
    item_cart_quantity =driver.find_element(By.XPATH,"//div[@class='cart_quantity']")

    assert item_cart_quantity.text == '1'
    assert item_name_in_cart == product_title_card
    assert item_description_cart == item_description_card
    assert item_price_cart == item_price_card



def test_product_backtoproducts(log_in):
    driver = log_in

    product_item = driver.find_element(By.XPATH,
                                       "//a[@id ='item_4_title_link']/div[@class ='inventory_item_name ']")

    product_item.click()
    back_to_products_button = driver.find_element(By.XPATH,"//button[@data-test = 'back-to-products']")
    back_to_products_button.click()

    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

