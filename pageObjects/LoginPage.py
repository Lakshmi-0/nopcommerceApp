from selenium import webdriver
from selenium.webdriver.common.by import By


class LoginPage:
    textbox_username_id = "//input[@id='Email']"
    textbox_password_id = "//input[@id='Password']"
    button_login_xpath ="//button[@class='button-1 login-button']"
    link_logout_linktext ="//a[text()='Logout']"

    def __init__(self,driver):
        self.driver = driver

    def setUserName(self,username):
        self.driver.find_element("xpath",self.textbox_username_id).clear()
        self.driver.find_element("xpath",self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element("xpath",self.textbox_password_id).clear()
        self.driver.find_element("xpath",self.textbox_password_id).send_keys(password)

    def clickLogin(self):
        self.driver.find_element("xpath",self.button_login_xpath).click()

    def clickLogout(self):
        self.driver.find_element("xpath",self.link_logout_linktext).click()



