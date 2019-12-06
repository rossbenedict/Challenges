import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge2(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_challenge2(self):
        self.driver.get("https://www.copart.com")

        #print(self.driver.title)
        #html=self.driver.page_source
        #print(html)

        self.searchfield = self.driver.find_element(By.ID, "input-search")
        self.searchfield.click()
        self.searchfield.send_keys('Exotics')
        self.searchbutton = self.driver.find_element(By.XPATH, '//*[@id="search-form"]/div/div[2]/button')
        self.searchbutton.click()

        #from mentor
        WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr[1]/td[5]/span')))
        assert ("PORSCHE", self.driver.find_element(By.XPATH, '//*[@id="serverSideDataTable"]/tbody/tr[1]/td[5]/span'))

        #from class
        datawait = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, '//*[@id=\"serverSideDataTable\"]/tbody/tr[1]//td')))
        datatable = self.driver.find_element(By.XPATH, '//*[@id=\"serverSideDataTable\"]/tbody/tr[1]//td'))
        self.assertIn("PORSCHE", datatable)


        #From class
        #html=self.driver.page_source
        #print(html)
        #self.assertIn("PORSCHE", html)

if __name__ == '__main__':
    unittest.main()