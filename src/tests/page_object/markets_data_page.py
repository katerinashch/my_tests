from src.tests.page_object.base_page import BasePage
from src.tests.page_object.table_content import TableContent
import re
#from selenium.webdriver.support.ui import Select
from selenium.webdriver import ActionChains


class MarketsDataPage(BasePage):
    
    screener_title = "Global equity screener - FT.com"
    
    def open(self, driver):
        self.browser = driver
        self.browser.get("http://markets.ft.com/research/markets/overview")
        
    def has_label(self, xpath, label_pattern):  
        label = self.browser.find_element_by_xpath(xpath).text
        self.assertEqual(label, label_pattern, "Incorrect label")
        print label   
        
    def get_table_content(self, table_sector_xpath):
        table = self.browser.find_element_by_xpath(table_sector_xpath)
        pattern = '[a-zA-Z]* *[a-zA-Z]'
        content = TableContent()
        
        for td in table.find_elements_by_tag_name('td'):
            if re.search(pattern, td.text):
                content.names.append(td.text)
            else:
                content.values.append(td.text)
        
        return content
        
    def move_roller(self, xpath, xoffset):
        actionChains = ActionChains(self.browser)
        elem = self.browser.find_element_by_xpath(xpath)
        actionChains.drag_and_drop_by_offset(elem, xoffset, 0).perform()
    
    def push_the_buttons(self, xpathes):
        for source in xpathes: 
            button = self.browser.find_element_by_xpath(source)
            button.click()     
        
