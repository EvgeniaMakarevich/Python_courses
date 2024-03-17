import time

from selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    return driver


def test_add_remove(driver):
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    add = driver.find_element(By.XPATH,'//*[@id="content"]/div/button')
    add.click()
    delay = WebDriverWait(driver,10).until(EC.visibility_of_element_located((By.XPATH,'//*[@id="elements"]/button')))
    assert delay.is_displayed()
    assert delay.is_enabled()

    add.click()
    delays = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH,"//button[@class = 'added-manually']")))
    assert len(delays) == 2

    for x in delays:
        x.click()

    WebDriverWait(driver, 10).until_not(
        EC.visibility_of_any_elements_located((By.XPATH, "//button[@class='added-manually']")))

    # После исчезновения кнопок, выполните проверку их отсутствия
    remaining_delays = driver.find_elements(By.XPATH, "//button[@class='added-manually']")
    assert len(remaining_delays) == 0








