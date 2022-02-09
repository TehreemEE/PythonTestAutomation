from selenium import webdriver
import unittest
import HtmlTestRunner
import time
from selenium.webdriver.common.by import By
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))
from AutomationTests.POM.Pages.homePage import HomePage
from AutomationTests.POM.Pages.loginPage import LoginPage
from AutomationTests.POM.Pages.dashboardPage import DashboardPage
from AutomationTests.POM.Pages.contractDetailPage import ContractDetailPage


class RaiseBreach(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        #cls.driver=webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")
        cls.driver = webdriver.Firefox(executable_path="C:/Drivers/geckodriver-v0.30.0-win64/geckodriver.exe")
        cls.driver.maximize_window()

    def test_raise_breach(self):
        driver = self.driver

        driver.get("http://localhost:9000/")

        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

        login = LoginPage(driver)
        login.enter_email("evita.abishag@last-shipment.com")
        login.enter_password("ypgb62T9pMmPuFHd")
        login.click_login()
        time.sleep(3)
        # message = driver.find_element(By.XPATH, "//h1[contains(text(),'User Dashboard')]").text
        # self.assertEqual(message, "User Dashboard")
        print("User is authenticated")

        dashboard = DashboardPage(driver)
        time.sleep(3)
        dashboard.click_last_contract()

        description = ContractDetailPage(driver)
        description.enter_description("Contract needs to be reviewed")
        description.click_submit_breach()
        time.sleep(2)
        print("Breach submitted")

        message = driver.find_element(By.XPATH, "//em[contains(text(),'a56eb3aa-5a6e-493c-9972-d4986e3ef598')]").text
        self.assertEqual(message, "a56eb3aa-5a6e-493c-9972-d4986e3ef598")
        print("the same Contract View is displayed")

        message = driver.find_element(By.XPATH, "//td[contains(text(),'Contract needs to be reviewed')]").text
        self.assertEqual(message, "Contract needs to be reviewed")
        print("created breach is available")


    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print("Test Completed")


if __name__ == "__main__":
    unittest.main(
        testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/AAI/equitime_24012022_TehreemFatima/Reports"))
