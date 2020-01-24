from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class filters:
    def __init__(self):
        self.driver = driver
        print("initialize filter")

    def clickFilter(self, filterName):
        self.sectionNum = indexinLoop
        print("click on filter name = " + filterName)

    def filtersSearchText(self, filtersBy):
        print("searching filter section by text" + filtersBy)

    def clickFiltersCheckbox(self, checkboxValue):
        ckbx = self.driver.find_element('//*[@id="lot_model_desc' + checkboxValue + '"]')
        #
        print("checkboxvalue = " + checkboxValue)

    def getAllFilterCheckboxes(self):
        listofcheckboxevalues = self.driver.find_element(By.XPATH, '//*[@id="collapse' + self.sectionNum + '"]//li')
        return listofcheckboxevalues