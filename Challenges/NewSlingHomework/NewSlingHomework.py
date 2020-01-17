import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class NewSlingHomework(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.sling.com")

    def tearDown(self):
        self.driver.close()

    def test_NewSlingHomework(self):

        #count how many alttags are on the page
        # //*  gives 1825 elements
        # search for alt
        # how many alt text and what the not alt stuff is
        #name this sling homeworkalt
        #used challenge 3

        time.sleep((10))
        elements = self.driver.find_elements(By.XPATH, "//*")
        tags = []
        for e in elements:
            print(e.tag_name)
            print(e.get_attribute("alt"))
            tags.append(e.tag_name)
#c users pycharmprojects add chromedriver.exe into project

        if ("img" || "svg")
            is there an alt tag.
                imagaltcount =+1
                print(e.get_attribute(("alt")))







if __name__ == '__main__':
    unittest.main()