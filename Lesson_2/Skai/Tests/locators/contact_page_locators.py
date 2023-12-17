from selenium.webdriver.common.by import By


class Fields_locators:
    url = "https://skaistaging.wpengine.com/contact-us-new/"
    name_input = (By.XPATH, '//*[@id="pardot-form-firstname"]')
    lastname_input = (By.XPATH, '//*[@id="pardot-form-lastname"]')
    email_input = (By.XPATH, '//*[@id="pardot-form-email_address"]')
    company_input = (By.XPATH, '//*[@id="pardot-form-company"]')
    job_title_input = (By.XPATH, '//*[@id="pardot-form-job_title"]')
    area_of_int = (By.XPATH, "//button[@data-id = 'pardot-form-channels']")
    m_dig_spend = (By.XPATH, "//button[@data-id = 'pardot-form-ad_spend']")
    country = (By.XPATH, "//button[@data-id ='pardot-form-country']")
    state = (By.XPATH, "//button[@data-id ='pardot-form-state']")
    questions = (By.XPATH, '//*[@id="pardot-form-comments"]')
    how_heard = (By.XPATH, "//button[@data-id = 'pardot-form-How_Did_You_Hear_About_Us']")
    area_of_int_pot_options = "//button[@data-id ='pardot-form-channels']/following-sibling::div/ul/li"
    m_dig_spend_options = "//button[@data-id ='pardot-form-ad_spend']/following-sibling::div/ul/li"
    country_option_usa = "//button[@data-id ='pardot-form-country']/following-sibling::div/ul/li[2]"
    state_options = "//button[@data-id ='pardot-form-state']/following-sibling::div/ul/li"
    how_heard_options = "//button[@data-id ='pardot-form-How_Did_You_Hear_About_Us']/following-sibling::div/ul/li"


class Button:
    button_contact_us = '//*[@id="pardot-form"]/div[15]/input'


