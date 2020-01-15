import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Common.TopNavSearch import *
#remember to import classes

class Challenge5(unittest.TestCase):

    # def __init__(self, methodName: str = ...):
    #     super().__init__(methodName: self.driver = None str = ...)

    def setUp(self):
        self.driver = webdriver.Chrome("../chromedriver")

    def tearDown(self):
        self.driver.close()

    def test_callenge5(self):
        s = TopNavSearch(self.driver)
        s.runSearch("porsche")
        # self.assertIn  #from challenge 2

        # query = "honda"
        # s.runSearch(query)
        #assert from challenge 2   self.assertIn(query.upper(),

        #now put into for loop
        queryList = ["porsche", "honda", "ford"]
        for query in queryList:
            s.runSearch(query)
            #self.assert

        # queryList = ["porsche", "honda", "ford"]
        # modelslist = []
        # listofelements = driver.findlements(By.XPATH, "//tbody//spand{@data-uname='lotsearchLotmodel']")
        # for e in listofelements:
        #     modelslist.append(e.text)

        print(queryList)

        #this will populate modelslist
        #modelslist.sort()

        #sorts the list alphabetically?
        #compare a element to b element if = 2 of that element if differnt then start new count
        #if else in loop
        #output there x of this model

        #second part
        #look at damage types from copart and challenge
        #create count into the different damage types


        #python switch/case   create a class and methods for decision tree
        #place these in a dictionary
        #techbeamers.com/python-switch-case
        #convert into a class?
        #create a reusable switch method
        #focus on a small set of data
        # get data print out dictionary and then add it to you code soe you don't have run it all again.
        #reportportal.io

    #make dictionary


if __name__ == '__main__':
    unittest.main()



# class see w3schools
#   _init_ is created for you
#     Or you can specify
#
# Challenge 3 sets up a webdriver for chrome
#     to get the search
#         break it into a search Method
#
#     Create a common method/Method
#
#     new python file TopNavSearch
