import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Bonus(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")


    def tearDown(self):
        self.driver.close()

    def test_bonus1(self):
        self.driver.get("https://www.sling.com")
        self.assertIn("Sling", self.driver.title)
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"channelList\"]//img")

        i = 0
        while i < len(elements):
            print(elements[i].get_attribute("src") + " - " + elements[i].get_attribute("alt"))
            i += 1


    def test_bonus2(self):
        self.driver.get("https://www.sling.com/search")
        self.assertIn("Sling", self.driver.title)
        element = self.driver.find_element(By.XPATH, '//*[@aria-label=\"input for search\"]')
        element.click()
        element.send_keys("Speed Racer")
        element.send_keys(Keys.RETURN)
        #other = self.driver.find_element(By.XPATH, '//*[@id=\"searchWrapper\"]/div[contains(@class,\'sc-isojaI joJasG\']' )
        #othersubmit()

        html = self.driver.page_source
        #print(html)
        self.assertIn("Speed Racer", html)


if __name__ == '__main__':
    unittest.main()





