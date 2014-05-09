'''
Created on Apr 11, 2014

@author: EkaterinaSh
'''
from src.tests.page_object.base_page import BasePage

#import time

class LoginPage(BasePage):
    
    
    def perform_login(self, driver, page_link, u_mail, u_pwd):
        self.browser = driver
        self.browser.get(page_link)
        
        sign_in = self.browser.find_element_by_id("ftLogin-signIn")
        
        username = self.browser.find_element_by_id("ftLogin-username")
        password = self.browser.find_element_by_id("ftLogin-password")
        submit = self.browser.find_element_by_xpath("//div[@id='ftLogin-box']/form/fieldset[3]/p/button")
   
        sign_in.click()
        username.send_keys(u_mail)
        password.send_keys(u_pwd)
        submit.click()
        return self.browser
    
    def get_user_login(self):
        user_name= self.browser.find_element_by_id("ftLogin-user").text
        return user_name
        
    
