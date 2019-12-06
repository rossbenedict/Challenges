import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge1(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge1(self):
        self.driver.get("https://www.google.com")
        self.assertIn("Google", self.driver.title)


    def test_challenge2(self):
        self.driver.get("https://www.copart.com")

        self.searchfield = self.driver.find_element(By.ID, "input-search")
        self.searchfield.click()
        self.searchfield.send_keys('Porsche')
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(By.CSS_SELECTOR, 'btn btn-lightblue'))
        #self.driver.find_element(By.CSS_SELECTOR, 'btn btn-lightblue').click()




if __name__ == '__main__':
    unittest.main()
