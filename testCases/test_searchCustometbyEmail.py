import time

import pytest

from pageObjects.AddcustomerPage import AddCustomer
from pageObjects.LoginPage import LoginPage
from pageObjects.SearchCustomerPage import SearchCustomer
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_SearchCustomerByEmail_004:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail1()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen() # Logger

    @pytest.mark.regression
    def test_searchCustomerByEmail(self,setup):
        self.logger.info("*****************Test_SearchCustomerByEmail_004**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        self.logger.info("*********Login Successful***********")

        self.logger.info("************Starting Search Customer By Email***********")

        self.addCust = AddCustomer(self.driver)
        self.addCust.clickOnCustomerMenu()
        self.addCust.clickOnCustomerMenuItem()

        self.logger.info("************Searching Customer By Email***********")

        search_customer = SearchCustomer(self.driver)
        search_customer.setEmail("brenda_lindgren@nopCommerce.com")
        search_customer.clickOnSearch()
        time.sleep(5)
        status = search_customer.searchCustomerByEmail("brenda_lindgren@nopCommerce.com")
        assert True == status
        self.logger.info("**********************TC_Test_SearchCustomerByEmail_004 is Finished")
        self.driver.close();