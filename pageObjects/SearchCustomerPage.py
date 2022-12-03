
class SearchCustomer:
    # Add Customer page
    txtEmail_id = "//input[@id='SearchEmail']"
    txtFirstName_id = "//input[@id='SearchFirstName']"
    txtLastName_id = "//input[@id='SearchLastName']"
    btnSearch_id = "//button[@id='search-customers']"

    tableSearchResult_xpath = "//table[@role='grid']"
    table_xpath = "//table[@id='customers-grid']"
    tableRows_xpath = "//table[@id='customers-grid']//tbody/tr"
    tableColumns_xpath ="//table[@id='customers-grid']//tbody/tr/td"

    def __init__(self,driver):
        self.driver = driver

    def setEmail(self,email):
        self.driver.find_element("xpath",self.txtEmail_id).clear()
        self.driver.find_element("xpath",self.txtEmail_id).send_keys(email)

    def setFirstName(self,fname):
        self.driver.find_element("xpath", self.txtFirstName_id).clear()
        self.driver.find_element("xpath", self.txtFirstName_id).send_keys(fname)

    def setLastName(self,lname):
        self.driver.find_element("xpath", self.txtLastName_id).clear()
        self.driver.find_element("xpath", self.txtLastName_id).send_keys(lname)

    def clickOnSearch(self):
        self.driver.find_element("xpath",self.btnSearch_id).click()

    def getNoOfRows(self):
        rows_list =[]
        rows_list = self.driver.find_element("xpath","//table[@id='customers-grid']//tbody/tr").text
        return len(rows_list)

    def getNoOfCloumns(self):
        col_list=[]
        cols_list= self.driver.find_element("xpath",self.tableColumns_xpath).text
        return len(cols_list)

    def searchCustomerByEmail(self,email):
        flag=False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element("xpath",self.table_xpath)
            emailid = table.find_element("xpath","//table[@id='customers-grid']//tbody/tr["+str(r)+"]/td[2]").text
            if emailid == email:
                flag=True
                break
        return flag

    def searchCustomerByName(self,Name):
        flag = False
        for r in range(1,self.getNoOfRows()+1):
            table=self.driver.find_element("xpath",self.table_xpath)
            name = table.find_element("xpath","//table[@id='customers-grid']/tbody/tr["+str(r)+"]/td[3]").text
            if name == Name:
                flag=True
                break
        return flag
