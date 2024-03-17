from selenium import webdriver
import pytest
from selenium.webdriver.chrome.webdriver import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Python_courses.Lesson_3.HW_waits.data import Urls,Data
from Python_courses.Lesson_3.HW_waits.locators import Before_log_in,Login
@pytest.fixture
def options():
    options = Options()
    options.add_argument('--start-maximized')
    return options


@pytest.fixture
def driver(options):
    driver = webdriver.Chrome(options=options)
    driver.implicitly_wait(10)
    yield driver
    driver.quit()


def test_log_in(driver):
    driver.get(Urls.url)
    assert driver.find_element(By.XPATH, Before_log_in.h1).text == Data.h1_text

    driver.find_element(By.XPATH, Before_log_in.button).click()

    # wait.until(EC.visibility_of_element_located((By.XPATH, Login.login))).send_keys('login')
    # wait.until(EC.visibility_of_element_located((By.XPATH, Login.password))).send_keys('password')
    # checkbox = wait.until(EC.visibility_of_element_located((By.XPATH, Login.checkbox)))
    # checkbox.click()
    # assert checkbox.is_selected()
    # wait.until(EC.element_to_be_clickable((By.XPATH, Login.register))).click()
    # loder = wait.until(EC.visibility_of_element_located((By.XPATH, "//div[@id = 'loader']")))
    # assert loder.is_displayed()
    # assert wait.until(EC.visibility_of_element_located((By.XPATH, "//p[@id = 'successMessage']"))).text == 'Вы успешно зарегистрированы!'