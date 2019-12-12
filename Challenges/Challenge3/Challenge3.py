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
        print("Makes/Models")
        for x in range(1, 5):
            oneloop = str(x)
            for i in range(1, 6):
                twoloop = str(i)
                carMake = self.driver.find_element(By.XPATH, '//*[@id=\"tabTrending\"]/div[1]/div[2]/div['+oneloop+']/ul/li['+twoloop+']/a')
                carLink = carMake.get_attribute("href")

                if x <= 2:
                    print(carLink[37:] + " - " + carLink)
                else:
                    print(carLink[36:] + " - " + carLink)

        print(" ")
        print(" ")




    def test_challenge3whileloop(self):
        self.driver.get("https://www.copart.com")
        print("Categories")
        firstLoop = 1

        while firstLoop < 5:
            secondLoop = 1
            aLoop = str(firstLoop)
            while secondLoop < 6:
                bLoop = str(secondLoop)
                searchCategory = self.driver.find_element(By.XPATH, '//*[@id=\"tabTrending\"]/div[3]/div['+aLoop+']/ul/li['+bLoop+']/a')
                grabbedCat = searchCategory.get_attribute("href")

                searchtag = self.driver.find_element(By.CSS_SELECTOR, '#tabTrending > div:nth-child(4) > div:nth-child('+aLoop+') > ul > li:nth-child('+bLoop+') > a')
                taggrab = searchtag.get_attribute("text")

                print(taggrab + " - " + grabbedCat)
                secondLoop += 1

            firstLoop += 1


        #find elements
        #relative remove stuff and add / on xpath
        #only want makes and models with for loop
        #    popular searches
        #Categories with a while loop

        #how to grab HREF, get attribute

        #screen contatenation
        #xrchiang@gmail.com personal email



if __name__ == '__main__':
    unittest.main()