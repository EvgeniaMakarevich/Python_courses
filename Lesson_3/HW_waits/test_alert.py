from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Python_courses.Lesson_3.HW_waits.data import Urls,Data
from Python_courses.Lesson_3.HW_waits.locators import Before_log_in,Login
import pyautogui
import time
# from pywinauto.application import Application




@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver


# def test_alert(driver):
#     driver.get('https://the-internet.herokuapp.com/basic_auth')
#     time.sleep(2)
#     app = Application().connect(title='Sign in')
#     alert = app.window(title='Sign in')
#
#     alert['Username'].type_keys('admin')
#     alert['Password'].type_keys('admin')
#
#     alert['Sing in'].click()
#

def test_alert(driver):
    driver.get('https://the-internet.herokuapp.com/basic_auth')
    time.sleep(2)

    driver.switch_to.alert.send_keys('admin')
    # alert.send_keys('admin')  # Вводим имя пользователя
    # alert.send_keys('\t')  # Переходим на следующее поле (в зависимости от интерфейса)
    # alert.send_keys('admin')  # Вводим пароль
    # alert.accept()  # Принять (или можно использовать alert.dismiss() для отмены)
    # driver.find_element(By.NAME,'Username').send_keys('admin')
    time.sleep(3)



