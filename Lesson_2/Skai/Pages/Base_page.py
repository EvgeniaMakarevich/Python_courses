from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
from faker import Faker


class Base_page:

    def __init__(self, driver, url):
        self.driver = driver
        self.url = url


    def open(self):
        self.driver.get(self.url)



    def borlabs_banner_close(self):
        borlabs_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='_brlbs-btn _brlbs-btn-accept-all _brlbs-cursor']"))
        )
        borlabs_button.click()


    def select_random_option_from_dropdown(self, dropdown_locator,options_locator):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dropdown_locator)
        )
        dropdown.click()

        options = WebDriverWait(self.driver, 10).until(
              EC.visibility_of_all_elements_located((By.XPATH, options_locator)))

        random_index = random.randint(1, len(options) - 1)
        options[random_index].click()


    def select_exact_option(self,dropdown_locator,option_locator):
        dropdown = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(dropdown_locator))
        dropdown.click()
        option = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, option_locator)))
        option.click()


    def submit_form(self,button_locator):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH,button_locator))).click()



