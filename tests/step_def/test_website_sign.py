

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, parsers, given, when ,then
import pytest

scenarios('../features/web_UI.feature')



@pytest.fixture
def browser():
    b=webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\chromedriver_win32\chromedriver.exe")
    b.implicitly_wait(10)
    yield b
    b.quit()
#
#homepage

@given('home page')
def home_page(browser):
    browser.get("https://www.browserstack.com/users/sign_in")

@when('the user sign up for')
def search_pharse(browser):
    search_input=browser.find_element(By.XPATH,'//a[@href="/users/sign_up"]').click()    
    full_name=browser.find_element(By.ID,'user_full_name')
    full_name.send_keys('ahmed')
    b_email=browser.find_element(By.ID,'user_email_login')
    b_email.send_keys('ahmed.vip78@yahoo.com')
    pa_ssword=browser.find_element(By.ID,'user_password')
    pa_ssword.send_keys('ahmed.vip78#O')
    check_box_email=browser.find_element(By.NAME,'terms_and_conditions').click()
    submit_sign_doos=browser.find_element(By.XPATH,'//input[@name="commit" or @id="user_submit"]').click()



@then('the response contains result')
def result_phrase(browser):
    browser.implicitly_wait(10)
    final_check=browser.find_elements(By.XPATH,'//body[@id="confirmation"]')
    for phrase in final_check:
        assert phrase.text[0] == "C"










