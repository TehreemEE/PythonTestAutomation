#Class for Dashboard page which contains all the locators for page

from selenium.webdriver.common.by import By

class DashboardPage():

    def __init__(self,driver):
        self.driver= driver

        self.verify_text_xpath = "//h1[contains(text(),'User Dashboard')]"
        self.verify_text_xpath = "//h2[contains(text(),'Contracts')]"
        self.logout_button_xpath = "//button[contains(text(),'Logout')]"
        self.last_contract_xpath = "//tbody/tr[26]/td[6]/a[1]/i[1]"


    def click_logout(self):
        self.driver.find_element(By.XPATH, self.logout_button_xpath).click()

    def click_last_contract(self):
        self.driver.find_element(By.XPATH, self.last_contract_xpath).click()
