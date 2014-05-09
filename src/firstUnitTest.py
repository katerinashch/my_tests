'''
Created on Apr 7, 2014

@author: EkaterinaSh
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()

    def test_search_in_python_org(self):
        driver = self.browser
        driver.get("http://www.python.org")
        self.assertIn("Python", driver.title)
        elem = driver.find_element_by_name("q")
        elem.send_keys("selenium")
        elem.send_keys(Keys.RETURN)

    def tearDown(self):
        self.browser.close()

if __name__ == "__main__":
    unittest.main()

