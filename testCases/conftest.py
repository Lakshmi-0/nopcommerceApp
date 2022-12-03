import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# "C:/Users/Pavan/Desktop/sai selenium python/chromedriver.exe"
# "C:/Users/Pavan/Desktop/sai selenium python/geckodriver.exe"



@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        ser=Service("C:/Users/Pavan/Desktop/sai selenium python/chromedriver.exe")
        driver = webdriver.Chrome(service=ser)
        print("Launching Chrome browser*******")
    elif browser == 'firefox':
        ser = Service("C:/Users/Pavan/Desktop/sai selenium python/geckodriver.exe")
        driver = webdriver.Firefox(service=ser)
        print("Launching Firefox browser*******")
    else:
        ser = Service("C:/Users/Pavan/Desktop/sai selenium python/msedgedriver.exe")
        driver=webdriver.Edge(service=ser)
    return driver


def pytest_addoption(parser):  #This will get the value from CLI/hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption('--browser')

# ####################  Pytest  HTML Report #########################
# It is hook used for Adding environment info to HTML Report


def pytest_configure(config):
    config._metadata['Project name'] = 'nop Commerce'
    config._metadata['Module Name'] = 'Customers'
    config._metadata['Tester'] = 'Laxmi'

#  It is hook used for delete/modify environment info to HTML Report
@pytest.mark.optinalhook
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME",None)
    metadata.pop("Plugins",None)

