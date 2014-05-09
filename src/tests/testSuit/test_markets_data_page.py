'''
Created on Apr 18, 2014

@author: EkaterinaSh
'''
import unittest
from src.tests.page_object.markets_data_page import MarketsDataPage
from src.tests.page_object.table_content import TableContent
from src.tests.page_object.xpaths import XPaths
from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time


class Test(unittest.TestCase, MarketsDataPage, TableContent):


    def setUp(self):
        self.browser = webdriver.Firefox()
        self.page = MarketsDataPage()
        self.page.open(self.browser)
        
        self.xpath = XPaths


    def tearDown(self):
        self.browser.quit()
        
    
    def test_asmoke(self):
                
        elements_names = self.page.get_elements_text(self.xpath.all_sections_paths)
        print elements_names
        #TODO add check for all sections 
        
        sectors_dropdown = Select(self.browser.find_element_by_xpath(self.xpath.select_sectors_industries))
#        print sectors_dropdown.options
        print [option.text for option in sectors_dropdown.options]

        #Check default value and label = Sectors
        sectors_options = ["Sectors", "Industries"]
        self.assertEqual(sectors_dropdown.first_selected_option.text, sectors_options[0], "'Sectors' is not a default value")
        
        label = self.browser.find_element_by_xpath(self.xpath.sectors_label).text
        self.assertEqual(label, sectors_options[0], "Wrong label")
        print label
        
        #check Sector table 
        sectors_table_content = self.get_table_content(self.xpath.table_sectors_xpath)
        
        self.assertEqual(len(sectors_table_content.names), 10, "Names count is not 10")
        self.assertEqual(len(sectors_table_content.values), 10, "Values count is not 10")
        self.assertEqual(sectors_table_content.sectors_names_pattern.sort(), sectors_table_content.names.sort(), "Watch Sectors table content")
        
        print sectors_table_content.names
        print sectors_table_content.values
        
        #select industries and check label = Industries
        sectors_dropdown.select_by_visible_text(sectors_options[1])
        self.assertEqual(sectors_dropdown.first_selected_option.text, sectors_options[1], "'Industries' are not chosen")
        
        time.sleep(2)
        label_patterns = ["Top industries", "Bottom industries"]
        map(self.has_label, self.xpath.selected_industries_labels, label_patterns)

    def test_screener(self):
        
        self.browser.find_element_by_xpath(self.xpath.screener).click()
        self.assertEqual(self.browser.title, self.page.screener_title, "Wrong screener title")
        
        
        self.select_options(self.xpath.all_countries, "li", [2,3,5], self.xpath.country_suboptions, "input", [1, 3, 4] )
        self.select_options(self.xpath.all_sectors, "a", [7,11,5], self.xpath.sectors_suboptions, "input", [1, 2, 3])
        
        #Equity Attributes
        self.move_roller(self.xpath.market_cap_index1, 30)
        self.move_roller(self.xpath.market_cap_index2, -55)
        self.move_roller(self.xpath.beta_index1, 40)
        self.move_roller(self.xpath.beta_index2, -65)
        self.move_roller(self.xpath.dividend_index1, 50)
        self.move_roller(self.xpath.dividend_index2, -75)
        self.move_roller(self.xpath.pe_ratio_index1, 60)
        self.move_roller(self.xpath.pe_ratio_index2, -85)
        
        self.push_the_buttons(self.xpath.consensus_forecast)
        self.push_the_buttons(self.xpath.sell_activity)
        
        time.sleep(30)
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()