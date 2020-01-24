import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class headerSearch:
    def __init__(self):
        print("initializing headerSearch")

    def searchFor(selfself, query):
        print("search for query =" + query)

        searchfield = self.driver.find_element(By.ID, "input-search")
        searchfield.click()
        searchfield.send_keys(query)
        searchbutton = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[2]/button')
        searchbutton.click()

        dataelement = WebDriverWait(self.driver, 60).until(EC.presence_of_element_located(By.XPATH, "//*[@id=\"serverSideDataTble\"]//tbody"))

        tabledata = self.driver.find_element(By.XPATH,"//*[@id=\"serverSideDataTble\"]//tbody")
        visible = tabledata.text
        #slow down script to see what is there but do not use sleep
        print("visible")