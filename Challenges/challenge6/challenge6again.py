import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Common.headerSearch import headerSearch
from Common.filters import filters
from Common.searchResults import searchResults
from Common.screenShot import screenShot


class Challenge6again(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        print("in setup")
        self.driver.get("https://www.copart.com")

    def tearDown(self):
        # self.driver.close()
        print("in teardown")

    def test_challenge6again(self):
        try:
            hs = headerSearch(self.driver)
            hs.searchFor("nissan")
            # f = filters()
            # f.clickFilter('Model')
            # s = screenShot()
            # s.takeScreenShot("Skyline")
            # sr = searchResults
            # sr.changeDropDown("100")
        except:



if __name__ == '__main__':
    unittest.main()