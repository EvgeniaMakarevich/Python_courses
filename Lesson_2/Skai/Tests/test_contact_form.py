import pytest
from Python_courses.Lesson_2.Skai.Pages.contact_page import ContactPage
from Python_courses.Lesson_2.Skai.Tests.data.Contact_page_data import Url
from Python_courses.Lesson_2.Skai.Tests.locators.contact_page_locators import Fields_locators

def test_submit_contact_form(driver):
    contact_page = ContactPage(driver, Fields_locators.url)
    contact_page.open()
    contact_page.borlabs_banner_close()
    contact_page.fill_contact_form()
    contact_page.submit_contact_form()
    assert driver.current_url.startswith(Url.thankyou_page), 'Incorrect URL'
