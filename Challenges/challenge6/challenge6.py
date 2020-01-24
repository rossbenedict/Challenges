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

# error grab a screenshot
# where to store the screenshot
# write library to work on Mac and Windows
# create a folder and keep track of the path
# need to print out the full path and or open the image at the end
# Don't want to overwrite existing images
# recommend using the time stamp
# use imaging libraries like Pillow, not thread safe only does the on top browser
#so use whats build into the webdriver

#element screenshot_as_png
#screenshot_as_base64 saves as a string

#capture from Selenium
#driver.save_screenshot('/data/image.png")
#add how to save to a specific place

#capturing exceptions
    def trycatch(self):
        try:
            print(x)
        except NameError:
            print("an exception example")
        except:
            print("Something else went wrong")

        # go to copart, search, models enter a good model and check and then a bad model
        except BaseException as e:
            Screenshot().take(self.driver, challenge)
            sys.exit(e)

    def test_challenge6(self):
        try:
            filterName = "Model"
            #turn this next part into a class as well
            elements = self.driver.find_elements("//*[@id="filters-collapse-1"]//li//a[text()")
            count = 0
            for e in elements:
                count = count + 1
                if (e.text == filterName)
                    e.click()
            txtelement = self.driver.find_elements("//*[@id='collapseinside" + str(count) + "']/form/div/input")
            txtelement.send_keys("altima S")
            checkelement = self.driver.find_element("//*[@id='collapseinside" + str(count) + "']//abbr[@value='" + modelvalue + ";]")
            checkElement.click()
        except:
            print("an exception occurred")
            print("you wanted" + modelValue)
            print("but these are available checkboxes")

            checkboxelements= self.driver.find_elements(//*{@id='collapseinside4']//input{@types="checkbox"]//text(})
            for e in checkboxelements:
                e.get_attribute("alue")

            #change this to an object
            # gac = GetAllCheckboes()
            #gac.show()



#make a class to handle the filter
#go through the filter and click on the one you want
//*[@id="filters-collapse-1"]//li//a[text()

link text


