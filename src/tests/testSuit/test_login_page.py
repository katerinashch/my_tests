'''
Created on Apr 17, 2014

@author: EkaterinaSh
'''
import unittest
from src.tests.page_object.login_page import LoginPage
from selenium import webdriver


class Test(unittest.TestCase, LoginPage):
    


    def setUp(self):
        self.u_mail = "demuzka@gmail.com"
        self.u_pwd = "testmarket"
        self.page_link = "http://www.ft.com/home/europe"
        
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()


    def testName(self):
        page = LoginPage()
        logged_in_page = page.perform_login(self.browser, self.page_link, self.u_mail, self.u_pwd)
        title = logged_in_page.title
        print title

        self.assertIn( "World business, finance and political news from the Financial Times", title, "Wrong Title")
        user_name = page.get_user_login()
        print user_name
        
        self.assertEqual(user_name, self.u_mail, "Wrong user name")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()