from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from pytest_bdd import scenarios, parsers, given, when ,then
import pytest

CONVERTER={
    'phrase':str,
    'text':str
}
scenarios('../features/search_duck.feature',example_converters=CONVERTER)



@pytest.fixture
def browser():
    b=webdriver.Chrome(executable_path=r"C:\Users\Administrator\Desktop\chromedriver_win32\chromedriver.exe")
    b.implicitly_wait(10)
    yield b
    b.quit()

                                                  

@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    browser.get('https://duckduckgo.com/')


# When Steps

@when(parsers.parse('the user searches for "<text>"'))
def search_phrase(text,browser):
    search_input = browser.find_element_by_name('q')
    search_input.send_keys(text + Keys.RETURN)

# Then Steps

@then(parsers.parse('results are shown for "<phrase>"'))
def search_results(browser, phrase):
    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)
    links_div = browser.find_element_by_id('links')
    assert len(links_div.find_elements_by_xpath('//div')) > 0
    # Check search phrase
    search_input = browser.find_element_by_name('q')
    assert search_input.get_attribute('value') == phrase