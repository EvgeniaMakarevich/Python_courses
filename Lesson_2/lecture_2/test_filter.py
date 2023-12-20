import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


def test_filter(driver):
    driver.get('https://demoqa.com/sortable')
    list_elements = WebDriverWait(driver,10).until(EC.visibility_of_all_elements_located((By.XPATH, "//div[@class='vertical-list-container mt-4']/div")))
    action = ActionChains(driver)
    action.click_and_hold(list_elements[0]).move_to_element(list_elements[2]).release().perform()

    text = [x.text for x in list_elements[:3]]
    expected_text = ['Two', 'Three', 'One']
    assert text == expected_text

