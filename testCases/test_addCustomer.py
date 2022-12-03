import random
import string
import time
import pytest
from PIL import Image
from selenium.webdriver.common.by import By

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os


class Test_003_AddCustomer:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail1()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_addCustomer(self,setup):
        self.logger.info("************************Test_003_AddCustomer**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login Successful***********")

        self.logger.info("************Starting Add Customer Test***********")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuItem()

        self.addCust.clickOnAddNew()
        self.logger.info("******Providing customer information***********")

        self.email = random_generator() + '@gmail.com'
        self.addCust.setEmail(self.email)
        self.addCust.setPassword("test123")
        self.addCust.setFirstName("Naga")
        self.addCust.setLastName("laxmi")
        self.addCust.setDob("7/26/1981") # date format is MM/DD/YYYY
        self.addCust.setGender("Female")
        self.addCust.setCompanyName("MindQ")
        self.addCust.setCustomerRoles("Guests")
        self.addCust.setManagerOfVendor("Vendor 2")
        self.addCust.setAdminContent("This is for Testing Purpose ---------")
        self.addCust.clickOnSave()

        self.logger.info("************Saving customer file*******")

        self.logger.info("*******************Add Customer Validation started **********************")
        self.msg = self.driver.find_element("xpath",'//body').text
        print(self.msg) # The new customer has been added successfully.
        if 'customer has been added successfully.' in self.msg:
            assert True == True
            self.logger.info("**************Add customer test passed******")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_addCustomer_scr.png") # Screenshot
            assert True == False
            self.logger.info("**************Add customer test failed******")
        self.driver.close()
        self.logger.info("************Ending Test_003_AddCustomer Test************")


def random_generator(size=8, chars = string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))