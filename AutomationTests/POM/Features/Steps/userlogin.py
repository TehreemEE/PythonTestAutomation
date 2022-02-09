# UnitTest framework with BDD approach
from behave import *
from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.by import By
# Importing the page object models in the test file
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from AutomationTests.POM.Pages.homePage import HomePage
from AutomationTests.POM.Pages.loginPage import LoginPage
from AutomationTests.POM.Pages.dashboardPage import DashboardPage

#inheriting from the unittest class
class LoginTest(unittest.TestCase):

    @classmethod
    @given('user launch firefox browser')
    #steup function
    def setUpClass(context):
        # To open the web browser instance
        #context.driver = webdriver.Firefox(executable_path="C:/Drivers/geckodriver-v0.30.0-win64/geckodriver.exe")
        context.driver=webdriver.Firefox()
        context.driver.maximize_window()

    #Tests Functions
    @when('user open equitime homepage and click login button')
    def test_login_click(context):
        driver = context.driver
        # It will open the link for equitime application
        driver.get("http://localhost:9000/")
        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

    @when('Enter email "{username}" and password "{password}"')
    #Passing username and password as parameters to test steps and inputs are defined in the feature file
    def test_enter_credentials(context,username,password):
        login = LoginPage(context.driver)
        login.enter_email(username)
        login.enter_password(password)

    @when('Submits the form')
    def test_submit_form(context):
        login = LoginPage(context.driver)
        login.click_login()
        time.sleep(2)
        print("User is authenticated")

# This step is using exception handling for testing the valid and invalid login scenario
    @then('User must successfully login to dashboard and Company Dashboard, including all related company contracts, is available')
    def test_authentication(context):
        try:
            message = context.driver.find_element(By.XPATH, "//h1[contains(text(),'User Dashboard')]").text
        except:
            # If the "user dashboard" text is not found then the test will fail with invalid credentials
            context.driver.close()
            assert False,"Test Failed"
        #If no exception is thrown then below condition will verify the valid credentials and tests will pass
        if message == "User Dashboard":
            assert True, "Test Passed"

    @then('click logout button')
    def test_logout(context):
        dashboard = DashboardPage(context.driver)
        dashboard.click_logout()
        time.sleep(2)

    @then('close browser')
    def test_closebrowser(context):
        context.driver.close()

#Once the tests are completed, reports will generated using the following command
#behave -f allure_behave.formatter:AllureFormatter -o AutomationTestReports/ <Absoulte path to where feature files are available>
#Above command will generate reports in json format
#to save and review the reports in html use command "allure serve <Absolute path to reports folder>"
