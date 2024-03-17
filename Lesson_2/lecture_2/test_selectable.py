import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_selectable(driver):
    driver.get('https://demoqa.com/selectable')
    list_elements = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//ul[@id = 'verticalListContainer']/li")))
    for x in list_elements[:-1]:
        x.click()
    time.sleep(3)
    for x in list_elements[:-1]:
        assert 'mt-2 list-group-item active list-group-item-action' in x.get_attribute('class')
    list_element =  list_elements[-1]
    assert 'mt-2 list-group-item active list-group-item-action' not in list_element.get_attribute('class')


