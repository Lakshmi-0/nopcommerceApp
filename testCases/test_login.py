import pytest
from pageObjects.LoginPage import LoginPage
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
from Screenshot import Screenshot


class Test_001_Login:
    baseURL = ReadConfig.getApplicationURL()
    username = ReadConfig.getUseremail1()
    password = ReadConfig.getPassword()
    logger = LogGen.loggen()

    # @pytest.mark.regression
    def test_homePageTitle(self, setup):
        self.logger.info("*****************Test_001_Login*************************")
        self.logger.info("**********Verifying Home Page Title**********")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Your store. Login":
            assert True
            # self.driver.close()
            self.logger.info("************Home page title test is passed**************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_homepage_scr.png")  # Screenshot
            self.driver.close()
            self.logger.info("************Home page title test is failed**************")
            assert False
   # @pytest.mark.sanity
   # @pytest.mark.regression

    def test_login(self, setup):
        self.logger. info("*******************Verifying Login test**************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        act_title = self.driver.title
        self.driver.close()
        if act_title == "Dashboard / nopCommerce administration":
            assert True
            self.logger.info("*****************Login test is passed**************")
            #self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots\\" + "test_login_scr1.png")  # Screenshot
            self.logger.error("*******************Login test failed************")
            assert False
        self.driver.close()



