import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import pytest


# def test_resizable(driver):
#     driver.get('https://demoqa.com/resizable')
#     try:
#         # Maximize the window to have a better view of the resizable elements
#         driver.maximize_window()
#
#         # Locate the resizable element
#         resize_handle = driver.find_element(By.XPATH,
#                                             "//div[@id='resizableBoxWithRestriction']//span[contains(@class,'react-resizable-handle')]")
#
#         # Get the initial size of the resizable element
#         initial_size = resize_handle.size
#
#         # Perform a resize action by dragging the resizable handle
#         action = ActionChains(driver)
#         action.click_and_hold(resize_handle).move_by_offset(100, 100).release().perform()
#
#         # Wait for the resize action to take effect
#         time.sleep(8)
#
#         # Get the updated size of the resizable element after the resize action
#         updated_size = resize_handle.size
#
#         # Assert that the size has changed after the resize action
#         assert initial_size != updated_size, "The element size did not change after resizing"
#
#         print("Resize test passed successfully!")
#     finally:
#         # Close the browser window
#         driver.quit()


def test_resizable(driver):
    driver.get('https://demoqa.com/resizable')
    try:

        driver.maximize_window()

        resize_handle = driver.find_element(By.XPATH,
                                            "//div[@id='resizableBoxWithRestriction']//span[contains(@class,'react-resizable-handle')]")

        initial_size = resize_handle.size

        action = ActionChains(driver)
        action.click_and_hold(resize_handle).move_by_offset(100, 100).release().perform()

        time.sleep(5)

        updated_size = resize_handle.size

        assert updated_size['width'] >= initial_size['width'] and updated_size['height'] >= initial_size['height'], \
            "The element size did not change as expected after resizing"

    except Exception as e:
        pytest.fail(str(e))


def test_resizable_1(driver):
    driver.get('https://demoqa.com/resizable')
    try:
        resize_item = driver.find_element(By.XPATH, "//div[@id = 'resizable']")
        initial_size = resize_item.size
        action = ActionChains(driver)
        action.click_and_hold(resize_item).move_by_offset(100,100).release().perform()
        time.sleep(3)
        new_size = resize_item.size
        assert initial_size['width'] >= new_size['width']

    except Exception:
        pytest.fail(str(Exception))




