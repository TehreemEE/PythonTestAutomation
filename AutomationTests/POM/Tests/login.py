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


class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver=webdriver.Chrome(executable_path="C:/Drivers/chromedriver_win32/chromedriver.exe")
        cls.driver.maximize_window()

    def test_01_login_Evita(self):
        driver = self.driver

        driver.get("http://localhost:9000/")

        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

        login = LoginPage(driver)
        login.enter_email("evita.abishag@last-shipment.com")
        login.enter_password("ypgb62T9pMmPuFHd")
        login.click_login()
        time.sleep(2)
        message = driver.find_element(By.XPATH, "//h1[contains(text(),'User Dashboard')]").text
        self.assertEqual(message, "User Dashboard")
        print("User is authenticated")

        dashboard = DashboardPage(driver)
        dashboard.click_logout()

        time.sleep(2)

    def test_02_login_Alte(self):
        driver = self.driver

        driver.get("http://localhost:9000/")

        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

        login = LoginPage(driver)
        login.enter_email("alte.vsevolod@last-shipment.com")
        login.enter_password("eCtW7ZVkMKPmRy7F")
        login.click_login()
        time.sleep(2)
        message = driver.find_element(By.XPATH, "//h1[contains(text(),'User Dashboard')]").text
        self.assertEqual(message, "User Dashboard")
        print("User is authenticated")

        dashboard = DashboardPage(driver)
        dashboard.click_logout()

        time.sleep(2)

    def test_03_login_Amalija(self):
        driver = self.driver

        driver.get("http://localhost:9000/")

        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

        login = LoginPage(driver)
        login.enter_email("amalija.patrizio@smugglee.com")
        login.enter_password("77aPWK2sd665hXwP")
        login.click_login()
        time.sleep(2)
        message = driver.find_element(By.XPATH, "//h1[contains(text(),'User Dashboard')]").text
        self.assertEqual(message, "User Dashboard")
        print("User is authenticated")

        dashboard = DashboardPage(driver)
        dashboard.click_logout()

        time.sleep(2)

    def test_04_login_Phyllida(self):
        driver = self.driver

        driver.get("http://localhost:9000/")

        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

        login = LoginPage(driver)
        login.enter_email("phyllida.drest@luggagex.com")
        login.enter_password("HD3sdhY97PLfhRUr")
        login.click_login()
        time.sleep(2)
        message = driver.find_element(By.XPATH, "//h1[contains(text(),'User Dashboard')]").text
        self.assertEqual(message, "User Dashboard")
        print("User is authenticated")

        dashboard = DashboardPage(driver)
        dashboard.click_logout()

        time.sleep(2)

    def test_05_login_Elifalet(self):
        driver = self.driver

        driver.get("http://localhost:9000/")

        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

        login = LoginPage(driver)
        login.enter_email("elifalet.kunigunde@constructsy.com")
        login.enter_password("k6cQNtXv8BCaDxaw")
        login.click_login()
        time.sleep(2)
        message = driver.find_element(By.XPATH, "//h1[contains(text(),'User Dashboard')]").text
        self.assertEqual(message, "User Dashboard")
        print("User is authenticated")

        dashboard = DashboardPage(driver)
        dashboard.click_logout()

        time.sleep(2)

    def test_06_login_Lifaleth(self):
        driver = self.driver

        driver.get("http://localhost:9000/")

        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

        login = LoginPage(driver)
        login.enter_email("lifaleth.dejong@construct.com")
        login.enter_password("EPbU4tgvxPjTZT8d")
        login.click_login()
        time.sleep(2)
        message = driver.find_element(By.XPATH, "//h1[contains(text(),'User Dashboard')]").text
        self.assertEqual(message, "User Dashboard")
        print("User is authenticated")

        dashboard = DashboardPage(driver)
        dashboard.click_logout()

        time.sleep(2)

    def test_07_login_invalid(self):
        driver = self.driver

        driver.get("http://localhost:9000/")

        home = HomePage(driver)
        home.click_login()
        time.sleep(2)

        login = LoginPage(driver)
        login.enter_email("abc@abc.com")
        login.enter_password("123456")
        login.click_login()
        message = driver.find_element(By.XPATH, "//li[contains(text(),'user-not-found')]").text
        self.assertEqual(message, "user-not-found")
        time.sleep(2)
        print("User not found")

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        print ("Test Completed")

if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output="C:/Users/AAI/equitime_24012022_TehreemFatima/Reports"))





