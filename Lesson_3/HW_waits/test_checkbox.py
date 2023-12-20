import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

def test_checkboxes(driver):
    driver.get("https://the-internet.herokuapp.com/checkboxes")
    checkboxes = WebDriverWait(driver,10).until(EC.presence_of_all_elements_located((By.XPATH,"//input[@type = 'checkbox']")))
    assert len(checkboxes) == 2

    if checkboxes[1].is_selected():
        checkboxes[1].click()
    checkboxes[0].click()

    time.sleep(3)

    assert not checkboxes[1].is_selected()
    assert checkboxes[0].is_selected()

