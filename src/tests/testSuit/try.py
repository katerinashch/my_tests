'''
Created on Apr 22, 2014

@author: EkaterinaSh
'''
def test_select_sectors_industries(self):
       # select_sec_ind = "/html/body/div[4]/div[3]/div/div/div/div/div[4]/div[2]/div/div/h2/div[2]/div/select" 
       # sector = Select(self.browser.find_element_by_xpath(select_sec_ind))
#        print sector.options
#        print [option.text for option in sector.options]

        #Check default value and label = Sectors
        sector_options = ["Sectors", "Industries"]
      #  self.assertEqual(sector.first_selected_option.text, sector_options[0], "'Sectors' is not a default value")
        label = self.browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/table/thead/tr/th").text
        print label
        self.assertEqual(label, sector_options[0], "Wrong label")
        
        #select industries and check label = Industries
        #sector.select_by_visible_text(sector_options[1])
       # self.assertEqual(sector.first_selected_option.text, sector_options[1], "'Industries' are not chosen")
        
        label = self.browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/table/thead/tr/th").text
        print label
        self.assertEqual(label, "Top industries", "Wrong label")
        
        label = self.browser.find_element_by_xpath("/html/body/div[4]/div[3]/div/div/div/div/div[4]/div[2]/div/div[2]/div/div[2]/table/thead/tr/th").text
        print label
        self.assertEqual(label, "Bottom industries", "Wrong label")