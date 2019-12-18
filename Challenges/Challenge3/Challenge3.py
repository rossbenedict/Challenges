import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Challenge3(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")
        self.driver.get("https://www.copart.com")
        self.assertIn("Copart", self.driver.title)

    def tearDown(self):
        self.driver.close()


    def test_challenge3forloop(self):
        #self.driver.get("https://www.copart.com")
        print("Makes/Models")
        for x in range(1, 5):
            oneloop = str(x)
            for i in range(1, 6):
                twoloop = str(i)

                tagSearch = self.driver.find_element(By.CSS_SELECTOR,'#tabTrending > div:nth-child(2) > div:nth-child(2) > div:nth-child('+oneloop+') > ul > li:nth-child('+twoloop+') > a')
                tagResult = tagSearch.get_attribute("text")
                carLink = tagSearch.get_attribute("href")

                print(tagResult + " - " + carLink)



        print(" end of 1")
        print(" ")




    def test_challenge3whileloop(self):
        #self.driver.get("https://www.copart.com")
        print("Categories")
        firstLoop = 1

        while firstLoop < 5:
            secondLoop = 1
            aLoop = str(firstLoop)
            while secondLoop < 6:
                bLoop = str(secondLoop)

                #Second Attempt everything from Css Selector
                searchtag = self.driver.find_element(By.CSS_SELECTOR, '#tabTrending > div:nth-child(4) > div:nth-child('+aLoop+') > ul > li:nth-child('+bLoop+') > a')
                taggrab = searchtag.get_attribute("text")
                grabbedCat = searchtag.get_attribute("href")

                print(taggrab + " - " + grabbedCat)
                secondLoop += 1

            firstLoop += 1
        print(" end of 2")
        print(" ")

    def test_challenge3withIndexandforloop(self):
        #self.driver.get("https://www.copart.com")
        print("Makes/Models")

        catNum = len(self.driver.find_elements(By.XPATH, '//*[@id=\"tabTrending\"]/div[3]//a'))
        for newLoop in range(1, catNum):
            anewloop = str(newLoop)
            modelNum = len(self.driver.find_elements(By.XPATH, '//*[@id=\"tabTrending\"]/div[1]/div[2]/div['+ anewloop +']/ul//a'))
            for makeNum in range (1, modelNum):
                amakenum = str(makeNum)
                newSearch = self.driver.find_element(By.CSS_SELECTOR, '#tabTrending > div:nth-child(2) > div:nth-child(2) > div:nth-child('+ anewloop +') > ul > li:nth-child('+ amakenum +') > a')
                newResult = newSearch.get_attribute("text")
                newLink = newSearch.get_attribute("href")
                print(newResult + " - " + newLink)

        print(" end of 3")
        print(" ")



    def test_challenge3fromClass(self):
        #self.driver.get("https://www.copart.com")
        #self.assertIn("Copart", self.driver.title)
        elements = self.driver.find_elements(By.XPATH, "//*[@id=\"tabTrending\"]/div[1]//a")
        for count in elements:
            print(count.text + " - " + count.get_attribute("href"))
        print(" end of 4 - in class example")
        print(" ")

        #while loop
    def test_challenge3whilefromClass(self):
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

if __name__ == '__main__':
    unittest.main()