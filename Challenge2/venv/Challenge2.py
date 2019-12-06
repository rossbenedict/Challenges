import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By

class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")

        self.searchfield = self.driver.find_element(By.ID, "input-search")
        self.searchfield.click()
        self.searchfield.send_keys('Porsche')

        self.driver.find_element(By.CSS_SELECTOR, 'btn btn-lightblue').click()



if __name__ == '__main__':
    unittest.main()