from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pytest
from data import contact_us



def test_contact_us(test_form):
    driver = test_form
    # main_window = driver.current_window_handle
    #
    # driver.execute_script("window.open('https://skai.io/contact-us/', '_blank');")
    #
    # all_windows = driver.window_handles
    #
    # for window in all_windows:
    #     if window != main_window:
    #         driver.switch_to.window(window)
    #         break
    #
    # driver.get(contact_us)
    # time.sleep(5)
    # driver.switch_to.window(main_window)

