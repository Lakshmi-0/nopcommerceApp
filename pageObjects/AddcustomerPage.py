import time

from selenium.webdriver.support.select import Select


class AddCustomer:
    # Add customer Page
    lnkCustomers_menu_xpath = "//a[@href='#']//p[contains(text(),'Customers')]" # Main customer on dashboard
    linkCustomers_menu_item_xpath="//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]" # sub menu in customer on dashboard
    btn_Addnew_xpath = "//a[@class='btn btn-primary']" # Addnew button

    txtEmail_xpath = "//input[@id='Email']"
    txtPassword_xpath = "//input[@id='Password']"
    txtFirstName_xpath = "//input[@id='FirstName']"
    txtLastName_xpath = "//input[@id='LastName']"
    rdMaleGender_id = "//*[@id='Gender_Male']"
    rdFemaleGender_id = "//*[@id='Gender_Female']"
    txtDob_xpath = "//input[@id='DateOfBirth']"
    txtCompanyName_xpath = "//input[@id='Company']"
    txtcustomerRoles_xpath = "//div[@class='k-multiselect-wrap k-floatwrap']" # 2 are selecting
    listitemAdministrators_Xpath = "//li[contains(text(),'Administrators')]"
    listitemRegistered_xpath ="//li[contains(text(),'Registered')]"
    listitemGuests_xpath = "//li[contains(text(),'Guests')]"
    listitemvendors_xpath = "//li[contains(text(),'Vendors')]"
    drpmgrOfVendor_xpath = "//*[@id='VendorId']"
    txtAdminContent_xpath = "//textarea[@id='AdminComment']"
    btnSave_xpath = "//button[@name='save']" # Save button

    def __init__(self,driver):
        self.list_item = None
        self.driver = driver

    def clickOnCustomerMenu(self):
        self.driver.find_element("xpath",self.lnkCustomers_menu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element("xpath",self.linkCustomers_menu_item_xpath).click()

    def clickOnAddNew(self):
        self.driver.find_element("xpath",self.btn_Addnew_xpath).click()

    def setEmail(self,email):
        self.driver.find_element("xpath",self.txtEmail_xpath).send_keys(email)

    def setPassword(self,password):
        self.driver.find_element("xpath", self.txtPassword_xpath).send_keys(password)

    def setCustomerRoles(self,role):
        self.driver.find_element("xpath",self.txtcustomerRoles_xpath).click()
        time.sleep(3)
        if role == 'Registered':
            self.list_item = self.driver.find_element("xpath",self.listitemRegistered_xpath)
        elif role == 'Administrators':
            self.driver.find_element("xpath",self.listitemAdministrators_Xpath)
        elif role=='Guests':
            # Here user can be Registered (or) Guest, only one
            time.sleep(3)
            self.driver.find_element("xpath","//*[@id='SelectedCustomerRoleIds_taglist']/li/span[2]").click()
            self.list_item = self.driver.find_element("xpath",self.listitemGuests_xpath)
        elif role == 'Registered':
            self.list_item = self.driver.find_element("xpath",self.listitemRegistered_xpath)
        elif role == 'Vendors':
            self.list_item = self.driver.find_element("xpath",self.listitemvendors_xpath)
        else:
            self.list_item = self.driver.find_element("xpath", self.listitemGuests_xpath)
        time.sleep(3)
        # self.list_item.click();  # click is not work on variables
        self.driver.execute_script("arguments[0].click();",self.list_item)

    def setManagerOfVendor(self,value):
        drp=Select(self.driver.find_element("xpath",self.drpmgrOfVendor_xpath))
        drp.select_by_visible_text(value)

    def setGender(self,gender):
        if gender == 'Male':
            self.driver.find_element("xpath",self.rdMaleGender_id).click()
        elif gender == 'Female':
            self.driver.find_element("xpath",self.rdFemaleGender_id).click()
        else:
            self.driver.find_element("xpath", self.rdMaleGender_id).click()

    def setFirstName(self,fname):
        self.driver.find_element("xpath",self.txtFirstName_xpath).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element("xpath",self.txtLastName_xpath).send_keys(lname)

    def setDob(self,dob):
        self.driver.find_element("xpath",self.txtDob_xpath).send_keys(dob)

    def setCompanyName(self,cname):
        self.driver.find_element("xpath",self.txtCompanyName_xpath).send_keys(cname)

    def setAdminContent(self,content):
        self.driver.find_element("xpath",self.txtAdminContent_xpath).send_keys(content)

    def clickOnSave(self):
        self.driver.find_element("xpath",self.btnSave_xpath).click()