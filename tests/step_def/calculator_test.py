import unittest
from appium import webdriver

import nums_from_string

class calculator_test(unittest.TestCase):
    calcsession=None;
    calresult=None;
    def setUp(self):
        print("setup")
        desired_caps={}
        desired_caps["app"]="Microsoft.WindowsCalculator_8wekyb3d8bbwe!App"
        self.calcsession=webdriver.Remote(command_executor="https://127.0.0.1:4723", desired_capabilities=desired_caps)


    def teardown(self):
        print("teardown")
        self.calcsession.quit()

    def test_add(self):
        print("add")
        self.calcsession.find_element_by_name('One').click()
        self.calcsession.find_element_by_name('Two').click()
        self.calcsession.find_element_by_name('Equals').click()
        self.assertEqual(self.get_result(),'3')

    def test_substract(self):
        print("substract")

    def test_division(self):
        print("division")

    def get_result(self):
        phrase=self.calcsession.find_element_by_accessibility_id('CalculatorResults').text
        phrase_num=nums_from_string.get_nums(phrase)
        return phrase_num
    # find element by calss name 
    def calculator_catgory(Self,locator):
        self.calcsession.find_element_by_accessibility_id('TogglePaneButton').click()
        lists=find_element_by_accessibility_class_name('Microsoft.UI.Xaml.Controls.NavigationViewItem')

        for list in lists:
            if list.get_attribute('AutomationId') == locator:
                list.click()
                break    
    ## find_element by _xpath        
    def calculator_catgory_xpathh(self,locator)
    self.calcsession.find_element_by_accessibility_id('TogglePaneButton').click()
        lists=find_element_by_xpath('//ListItem]')

        for list in lists:
            if list.get_attribute('AutomationId') == locator:
                list.click()
                break
    def test_calcualtor_catgory(self):
        self.calculator_catgory('Graphing') 
           
    def test_calcualtor_catgory_xpath(self):
        self.calculator_catgory('Graphing')    
       