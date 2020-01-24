import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.NavigateTo import NavigateTo


class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()

    #element not found error figure out how to continue the test
    #creating a web crawler

    def test_challenge7(self):
        try:
            elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]//a")
            ng = NavigateTo(self.driver)
            for count in elements:
                if ng.goTo(count.get_attribute("href"), count.text):
                    #grab the url
                else:
        except:
            print("create your own action")
            # print(count.text + ": " + count.get_attribute("href"))

        #while loop
    def test_challenge7whilefromClass(self):
        #self.driver.get("https://www.copart.com")
        #self.assertIn("Copart", self.driver.title)
        #can be moved to setup along with assert

        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        i = 0
        while i < len(elements):
            print(elements[i].text + " - " + elements[i].get_attribute("href"))
            i += 1
        print(" end of 5 - in class example")
        print(" ")