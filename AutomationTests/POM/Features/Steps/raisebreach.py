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
from AutomationTests.POM.Pages.contractDetailPage import ContractDetailPage


class RaiseBreach(unittest.TestCase):

    @classmethod
    @given('user launch browser')
    def setUpClass(context):
        #context.driver = webdriver.Firefox(executable_path="C:/Drivers/geckodriver-v0.30.0-win64/geckodriver.exe")
        context.driver = webdriver.Firefox()
        context.driver.maximize_window()

    @when('User click login button on equitime homepage')
    def test_login_click(context):
        driver = context.driver
        driver.get("http://localhost:9000/")
        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

    @when('Enter valid credentials email "{username}" and password "{password}"')
    def test_enter_credentials(context, username, password):
        login = LoginPage(context.driver)
        login.enter_email(username)
        login.enter_password(password)

    @when('Submits the login form')
    def test_submit_form(context):
        login = LoginPage(context.driver)
        login.click_login()
        time.sleep(2)
        print("User is authenticated")

    @then('User should be logged in Company Dashboard, and all related company contracts, is available')
    def test_authentication(context):
        try:
            message = context.driver.find_element(By.XPATH, "//h1[contains(text(),'User Dashboard')]").text
        except:
            context.driver.close()
            assert False, "Test Failed"
        if message == "User Dashboard":
            assert True, "Test Passed"

    @when('User selects the last contract in the list by clicking contract view button on dashboard page')
    def test_clickcontract(context):
        dashboard = DashboardPage(context.driver)
        time.sleep(3)
        dashboard.click_last_contract()

    @then('contract details open')
    def test_contract_details(context):
        try:
            text = context.driver.find_element(By.XPATH, "//h3[contains(text(),'Details')]").text
        except:
            context.driver.close()
            assert False,"Test Failed"
        if text == "Details":
            assert True, "Test Passed"

    @then('User fills in a Breach Description and submits the breach form')
    def test_enter_description(context):
        description = ContractDetailPage(context.driver)
        description.enter_description("Contract needs to be reviewed")
        time.sleep(2)
        description.click_submit_breach()
        time.sleep(2)
        print("Breach submitted")

# This step is using exception handling for testing that same contract detail is opened when breach is created
    @then('the same Contract View is displayed')
    def test_verify_contract(context):
        try:
            contract_id = context.driver.find_element(By.XPATH, "//em[contains(text(),'a56eb3aa-5a6e-493c-9972-d4986e3ef598')]").text
        except:
            context.driver.close()
            assert False,"Test Failed"
        if contract_id == "//em[contains(text(),'a56eb3aa-5a6e-493c-9972-d4986e3ef598')]":
            assert True, "Test Passed"

# This step is using exception handling for testing that same contract detail is opened when breach is created
    @then('the created breach is present')
    def test_verify_breach(context):
        try:
            breach_description = context.driver.find_element(By.XPATH,"//td[contains(text(),'Contract needs to be reviewed')]").text
        except:
            context.driver.close()
            assert False, "Test Failed"
        if breach_description == "Contract needs to be reviewed":
                assert True, "Test Passed"

    @then('close the browser')
    def test_closebrowser(context):
        context.driver.close()
        print("Test Completed")

