#Class for Login page which contains all the locators for page

from selenium.webdriver.common.by import By

class ContractDetailPage():

    def __init__(self,driver):
        self.driver= driver

        self.description_xpath = "//textarea[@id='description']"
        self.submit_breach_xpath = "//button[contains(text(),'Submit breach')]"

    def enter_description(self,description):
        self.driver.find_element(By.XPATH, self.description_xpath).clear()
        self.driver.find_element(By.XPATH, self.description_xpath).send_keys(description)

    def click_submit_breach(self):
        self.driver.find_element(By.XPATH, self.submit_breach_xpath).click()

    def check_contract_details(self):
        contract = self.driver.find_element(By.XPATH, self.dashboard_details_message_xpath).text
        return contract

    def check_created_breach(self):
        breach = self.driver.find_element(By.XPATH, self.dashboard_details_breach_xpath).text
        return breach



