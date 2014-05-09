'''
Created on Apr 11, 2014

@author: EkaterinaSh
'''
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from src.tests.page_object.xpaths import XPaths
import time


class BasePage(object):
    
    def get_elements_text(self, xpaths):
        
        text = []
        for xpath in xpaths:
            elem = self.browser.find_element_by_xpath(xpath)
            text.append(elem.text)
        return text


    def select_options(self, option_xpath, option_tag_name, options_indices, suboption_xpath, checkbox_tag_name, checkbox_indices):
        countries_options_list = self.page.get_checkboxes_list(option_xpath, option_tag_name)
        
        for index in options_indices:
            countries_options_list[index].click()
            
            checkboxes_list = self.page.get_checkboxes_list(suboption_xpath, checkbox_tag_name)
            for index in checkbox_indices:
                checkboxes_list[index].click()

        
    def get_checkboxes_list(self, xpath, tag_name):
        try:
            ul = WebDriverWait(self.browser, 10).until(
        EC.presence_of_element_located((By.XPATH, xpath))    )
            return ul.find_elements_by_tag_name(tag_name)  
        except UnboundLocalError, expr:
            print "Element can't be found: ", expr
