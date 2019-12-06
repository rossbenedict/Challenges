import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()


    def test_challenge3forloop(self):
        self.driver.get("https://www.copart.com")
        elements = self.driver.find_elements(By.XPATH, "") #add xpath for popular searches


    def test_challenge3whileloop(self):
        self.driver.get("https://www.copart.com")
        elements = self.driver.find_elements(By.XPATH, "")  # add xpath above 3rd div  ./dive[3]//a
        #index each of them

        #find elements
        relative remove stuff and add / on xpath
        only want makes and models with for loop
            popular searches
        Categories with a while loop

        how to grab HREF, get attribute

        screen contatenation
        xrchiang@gmail.com personal email



if __name__ == '__main__':
    unittest.main()