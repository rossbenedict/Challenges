#import from chalenge 2
from selenium.webdriver.common.by import By

class TopNavSearch:
    def __init__(self, driver):
        self.driver = driver

    def runSearch(self, query):
        self.driver.get("https://www.copart.com")

        self.searchfield = self.driver.find_element(By.ID, "input-search")
        self.searchfield.click()
        self.searchfield.send_keys(query)
        self.searchbutton = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[2]/button')
        self.searchbutton.click()

#how to stay in the existing browser. line 8
#excersize the drop down on copart with number of results
#grab all of the data from the model column
#validate the set of data

#copart fives a good value
#//tbody//span[@data-uname=""]

#put values into a dictionary

    #def