from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
import time
import pytest
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Python_courses.Lesson_2 import Skai_forms_automation
from Python_courses.Lesson_2.Skai_forms_automation.data import username,password,verification_code,form_handlers
from Python_courses.Lesson_2.Skai_forms_automation.locators import pardot_username_field,pardot_password_field,pardot_login_button,verification_code_field,verification_button
# import pdb; pdb.set_trace()


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()



@pytest.fixture(scope = 'function')
def test_form(driver):
    driver.get('https://test.salesforce.com/?ec=302&startURL=%2Fsetup%2Fsecur%2FRemoteAccessAuthorizationPage.apexp%3Fsource%3DCAAAAYxnjeM3MDAwMDAwMDAwMDAwMDAwAAAA9rfX9i2VAZFeX8qNkROUVewlTKudN9PoiWgPfxNNT8VMrah3wmkJKF4wJ0QxR2UqNRjQI7mpSVhzs704xCyhFSZjZOdPwMbQGfUq9rRH52tMakVj1NnPDVFR_4HnGVR2fOwVExycSi6Wvr31M57dQiJTYMnKuonaZNCLXpHuV9eRG7V8_qGu4z1D8LoDLGt_HHVadmby0LrgrUG2cr_vCG2biSPjpVGR9QppqvI5tH4rv5LeEoLHOzub22RyULjFQotgKcXJtL-J8rt2lYqzY-Xmeu7aRQ8GsRsxnFDGYtvdNumYfowRFCKrYALG9t8cLcX3Qgp68IaoPkLfi1trbzYEDuSDS5cwMrjDbq0tdnjsW-NYwuPmK1Az9-gf3Dpq_Tu2Sa8bO3aLcBX641mRd9Pk0dUPgiB-IFGMI990qOWoC02WHdkqqly2o6yclN9TamS-TKhFb37mmiuA2bZFwSt805IvLGH0LAHLK0JvLFB9JhPn5EyKhLkVa2TyZ-itD6Oud_5NGY8yx7_Sdb2vts9cNI15uPI2R40nugdbWAgaePIJu2kgiM_fUrEsNXlwTYq6o99Ue1Czszie-rIsCiREtMrTi4ZtzV9FJ19qFjP7svjEFSlA-pnlf3I-1FCpbwIk7pihyA62CpRGW7uoq76TZtIM88TU91oIjaRA2IgqVKWStazYa150rARfDC4Toa4CDZTzBGkx4arifOW-nm9aUxOrRrB1TUNQFELbXz0V')
    driver.find_element(By.XPATH, '//*[@id="mydomainLink"]').click()
    driver.find_element(By.XPATH, '//*[@id="mydomain"]').send_keys('kenshoo')
    driver.find_element(By.XPATH, '//*[@id="mydomainContinue"]').click()

    username_field = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, pardot_username_field))
    )
    username_field.send_keys(username)
    driver.find_element(By.XPATH, pardot_password_field).send_keys(password)

    WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, pardot_login_button))).click()

    # pdb.set_trace()
    verification_field = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, verification_code_field)))

    verification_field.send_keys(verification_code)
    driver.find_element(By.XPATH,verification_button).click()
    time.sleep(7)
    driver.get(form_handlers)
    time.sleep(5)
    yield driver



