import pytest
import json
import time
import os
from datetime import datetime

# class to serve as a setup container
# best to be refactored...
class Setup():
    
    with open('testconfig.json') as config_file:
        config = json.load(config_file)

    seleniumhub = config['WEBDRIVER']['seleniumhub']
    desiredcapabilities = config['WEBDRIVER']['desiredcapabilities']

# driver object initialization
@pytest.fixture(scope="class")
def driver_init(request):
    from selenium import webdriver
    driver = webdriver.Remote(command_executor=Setup.seleniumhub, desired_capabilities=Setup.desiredcapabilities)
    driver.maximize_window()
    driver.implicitly_wait(60)
    driver.set_page_load_timeout(60)
    driver.set_script_timeout(60)
    request.cls.driver = driver
    yield
    driver.quit()

# driver object initialization
# object shared within the context of the class
@pytest.fixture(scope="session")
def driver_get(request):
    from selenium import webdriver
    driver = webdriver.Remote(command_executor=Setup.seleniumhub, desired_capabilities=Setup.desiredcapabilities)
    
    session = request.node
    
    for item in session.items:
        cls = item.getparent(pytest.Class)
        setattr(cls.obj,"driver",driver)
        driver.maximize_window()
        driver.implicitly_wait(60)
        driver.set_page_load_timeout(60)
        driver.set_script_timeout(60)
    yield
    driver.quit()

def pytest_generate_tests(metafunc):
    # called once per each test function, params injection
    funcarglist = metafunc.cls.params[metafunc.function.__name__]
    argnames = sorted(funcarglist[0])
    metafunc.parametrize(argnames, [[funcargs[name] for name in argnames]
            for funcargs in funcarglist])


@pytest.mark.usefixtures("driver_init")
class TestLoginSecurity(Setup):

    params = Setup.config['TESTCASES']['TestLoginSecurity']

    def test_step_111(self, url, username, screenshotpath):
        """System Test Case – System Access & Security: Step 1.1.1"""

        password = os.environ['PWD']
        
        self.driver.get(url)

        ############################
        # functionality test here...
        ############################


@pytest.mark.usefixtures("driver_get")
class TestLoginSecurityInvalid(Setup):

    params = Setup.config['TESTCASES']['TestLoginSecurityInvalid']

    def test_step_121(self, url, username, screenshotpath):
        """System Test Case – System Access & Security: Step 1.2.1"""

        password = os.environ['PWD']

        # Open URL
        self.driver.get(url)

        ############################
        # functionality test here...
        ############################


    def test_step_122(self, url, username, screenshotpath):
        """System Test Case – System Access & Security: Step 1.2.2"""

        password = os.environ['PWD']

        # Open URL
        self.driver.get(url)

        ############################
        # functionality test here...
        ############################


@pytest.mark.usefixtures("driver_init")
class TestPasswordSecurity(Setup):

    params = Setup.config['TESTCASES']['TestPasswordSecurity']

    def test_step_131(self, url, username, screenshotpath):
        """System Test Case – System Access & Security: Step 1.3.1"""

        password = os.environ['PWD']

        # Open URL
        self.driver.get(url)

        ############################
        # functionality test here...
        ############################


@pytest.mark.usefixtures("driver_get")
class TestTimeOutSecurity(Setup):

    params = Setup.config['TESTCASES']['TestTimeOutSecurity']

    def test_step_141(self, url, username, screenshotpath):
        """System Test Case – System Access & Security: Step 1.4.1"""

        password = os.environ['PWD']

        # Open URL
        self.driver.get(url)

        ############################
        # functionality test here...
        ############################


    def test_step_142(self, url, username, screenshotpath):
        """System Test Case – System Access & Security: Step 1.4.2"""

        ############################
        # functionality test here...
        ############################