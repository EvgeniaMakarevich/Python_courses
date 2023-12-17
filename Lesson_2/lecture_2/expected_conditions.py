import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from Python_courses.Lesson_2.lecture_2.Pages.InterecationPage import InteractionPage
from selenium.webdriver import ActionChains
class TestInteractions:

    def test_drag_and_drop(self, driver):
        page = InteractionPage(driver,'https://demoqa.com/droppable')
        page.open_browser()
        time.sleep(5)
        page.drop_simple()
        time.sleep(5)


    # def test_drag_and_drop(self,driver):
    #     driver.get('https://demoqa.com/droppable')
    #     action = ActionChains(driver)
    #     drag = driver.find_element(By.XPATH,'//*[@id="draggable"]')
    #     drop = driver.find_element(By.XPATH,'//*[@id="droppable"]')
    #     time.sleep(2)
    #     action.drag_and_drop(drag,drop)
    #     time.sleep(2)
    #     action.perform()
    #     text = driver.find_element(By.CSS_SELECTOR, '#droppable > p').text
    #     assert text == 'Dropped!'



    # def test_accept(self,driver):
    #     page = InteractionPage(driver, 'https://demoqa.com/droppable')
    #     page.open_browser()
    #     page.accept(driver)

    def test_accept(self, driver):
        driver.get('https://demoqa.com/droppable')
        wait = WebDriverWait(driver, 10)
        new_tab = driver.find_element(By.XPATH, '//*[@id="droppableExample-tab-accept"]')
        new_tab.click()

        acceptable = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="acceptable"]')))
        drop = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="droppable"]')))

        action = ActionChains(driver)
        action.drag_and_drop(acceptable, drop).perform()




