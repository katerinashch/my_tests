'''
Created on Apr 23, 2014

@author: EkaterinaSh
'''

class XPaths(object):
    #all sections on the page
    global_bench = "/html/body/div[4]/div[3]/div/div/div/div/div[4]/div/div/h2"
    sectors_idustries = "/html/body/div[4]/div[3]/div/div/div/div/div[4]/div[2]/div/div/h2/div"
    tool = "/html/body/div[4]/div[3]/div/div/div/div/div[3]/div/div/h2/div"
    equity_indices = "/html/body/div[4]/div[3]/div/div/div/div/div[2]/div/div/div/h2/div"
    data_archive = "/html/body/div[4]/div[3]/div/div/div/div/div[5]/div/div/div/h2"
    all_sections_paths = [global_bench, sectors_idustries, tool, equity_indices, data_archive]
    
    #Sectors sections
    select_sectors_industries = "//div[@id='wsod']/div[4]/div[2]/div/div/h2/div[2]/div/select"
    sectors_label = "//div[@id='wsod']/div[4]/div[2]/div/div[2]/div/div/table/thead/tr/th"
    table_sectors_xpath = "/html/body/div[4]/div[3]/div/div/div/div/div[4]/div[2]/div/div[2]/div/div/table/tbody"
    
    #industries sections 
    top_industries_label = "//div[@id='wsod']/div[4]/div[2]/div/div[2]/div/div/table/thead/tr/th"
    bottom_industries_label = "//div[@id='wsod']/div[4]/div[2]/div/div[2]/div/div[2]/table/thead/tr/th"
    
    selected_industries_labels = [top_industries_label, bottom_industries_label]
     
    #Screener
    screener = "//div[@id='wsod']/div[3]/div/div/div[3]/div/a[3]"
    
    all_countries = "//div[@id='wsod']/div/div/div/ul"
    country_suboptions = "//div[@id='wsod']/div/div[2]/ul"
    
    all_sectors = "//div[@id='wsod']/div[2]/div/div/ul"
    sectors_suboptions = "//div[@id='wsod']/div[2]/div[2]/ul"
    
    market_cap_index1 = "//div[@id='MarketCap']/div[2]/div/div[3]/div[2]/div[2]"
    market_cap_index2 = "//div[@id='MarketCap']/div[2]/div/div[3]/div[2]/div[3]"
    
    beta_index1 = "//div[@id='Beta5Year']/div[2]/div/div[3]/div[2]/div[2]"
    beta_index2 = "//div[@id='Beta5Year']/div[2]/div/div[3]/div[2]/div[3]"
    
    dividend_index1 = "//div[@id='DividendYield']/div[2]/div/div[3]/div[2]/div[2]"
    dividend_index2 = "//div[@id='DividendYield']/div[2]/div/div[3]/div[2]/div[3]"
    
    pe_ratio_index1 = "//div[@id='PEExclXItemsTTM']/div[2]/div/div[3]/div[2]/div[2]"
    pe_ratio_index2 = "//div[@id='PEExclXItemsTTM']/div[2]/div/div[3]/div[2]/div[3]"
    
    #Consensus forecast 
    button_buy = "//div[@id='ConsensusRecommendation']/div[2]/div/a[1]"
    button_out_perform = "//div[@id='ConsensusRecommendation']/div[2]/div/a[2]"
    button_hold = "//div[@id='ConsensusRecommendation']/div[2]/div/a[3]"
    button_under_perform = "//div[@id='ConsensusRecommendation']/div[2]/div/a[4]"
    button_sell = "//div[@id='ConsensusRecommendation']/div[2]/div/a[5]"
    button_no_rating = "//div[@id='ConsensusRecommendation']/div[2]/div/a[6]"
    
    consensus_forecast = [button_buy, button_out_perform, button_hold, button_under_perform, button_sell, button_no_rating]
    
    #Selling activity
    
    low = "//div[@id='DXScoreBucket']/div[2]/div/a[1]"
    medium = "//div[@id='DXScoreBucket']/div[2]/div/a[2]"
    high = "//div[@id='DXScoreBucket']/div[2]/div/a[3]"
    
    sell_activity = [low, medium, high]
    
    def __init__(self, params):
        '''
        Constructor
        '''
        