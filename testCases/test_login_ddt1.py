import time

import pytest
from PIL import Image
from pageObjects.LoginPage import LoginPage
from selenium import webdriver
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen
import os

from utilities import Excelutilis


class Test_002_DOT1_Login:
    baseURL = ReadConfig.getApplicationURL()
    path = ".//TestData/loginData.xlsx"
    logger = LogGen.loggen()


    @pytest.mark.regression
    def test_login_ddt(self, setup):
        self.logger.info("******************Test_002_DOT1_Login*****************")
        self.logger.info("*******************Verifying Login DDT test**************")
        self.driver = setup
        self.driver.get(self.baseURL)

        self.lp = LoginPage(self.driver)

        self.rows = Excelutilis.getRowCount(self.path,"Sheet1")
        print("No of Rows in a Excel:", self.rows)

        list_status=[] # empty list
        for r in range(2,self.rows+1):
            self.username=Excelutilis.readData(self.path,'Sheet1',r,1)
            self.password= Excelutilis.readData(self.path,'Sheet1',r,2)
            self.exp=Excelutilis.readData(self.path,'Sheet1', r,3)

            self.lp.setUserName(self.username)
            self.lp.setPassword(self.password)
            self.lp.clickLogin()
            time.sleep(5)

            act_title = self.driver.title
            exp_title = "Dashboard / nopCommerce administration"

            if act_title == exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****************Pass***")
                    self.lp.clickLogout();
                    list_status.append("Pass")
                elif self.exp == "Fail":
                    self.logger.info("***Failed**************")
                    self.lp.clickLogout();
                    list_status.append("Fail")
            elif act_title != exp_title:
                if self.exp == "Pass":
                    self.logger.info("*****************Failed**************")
                    list_status.append("Fail")
                elif self.exp == "Fail":
                    self.logger.info("*****************Passed**********")
                    list_status.append("Pass")

        if "Fail" not in list_status:
            self.logger.info("*********Login DDT test passed*********")
            self.driver.close()
            assert True
        else:
            self.logger.info("*********Login DDT test failed*********")
            self.driver.close()
            assert False

        self.logger.info("*****************End of Login DDT Test**************")
        self.logger.info("****************Completed TC_LoginDDT_002**********")
