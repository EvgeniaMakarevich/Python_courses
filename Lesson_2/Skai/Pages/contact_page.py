from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from Python_courses.Lesson_2.Skai.Pages.Base_page import Base_page
from Python_courses.Lesson_2.Skai.Tests.locators.contact_page_locators import Fields_locators,Button


fake = Faker()


class ContactPage(Base_page):
    def fill_contact_form(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.name_input)).send_keys('Test')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.email_input)).send_keys(fake.email())
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.lastname_input)).send_keys(fake.last_name())
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.company_input)).send_keys('Dizzain')
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.job_title_input)).send_keys('QA')
        self.select_random_option_from_dropdown(Fields_locators.area_of_int, Fields_locators.area_of_int_pot_options)
        self.select_random_option_from_dropdown(Fields_locators.m_dig_spend, Fields_locators.m_dig_spend_options)
        self.select_exact_option(Fields_locators.country,Fields_locators.country_option_usa)
        self.select_random_option_from_dropdown(Fields_locators.state,
                                                Fields_locators.state_options)
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(Fields_locators.questions)).send_keys(fake.text())
        self.select_random_option_from_dropdown(Fields_locators.how_heard, Fields_locators.how_heard_options)

    def submit_contact_form(self):
        return self.submit_form(Button.button_contact_us)