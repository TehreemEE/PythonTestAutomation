#Class for Home page which contains all the locators for page

from selenium.webdriver.common.by import By

class HomePage():

    def __init__(self,driver):
        self.driver= driver

        self.login_button_xpath = "//a[contains(text(),'Login')]"


    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()
