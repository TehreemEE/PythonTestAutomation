#Class for Login page which contains all the locators for page
from selenium.webdriver.common.by import By

class LoginPage():

    def __init__(self,driver):
        self.driver= driver

        self.email_textbox_id = "username"
        self.password_textbox_id = "password"
        self.login_button_xpath = "//button[contains(text(),'Submit')]"
        self.invalid_credentials_message_xpath = "//li[contains(text(),'user-not-found')]"

    def enter_email(self,email):
        self.driver.find_element(By.ID, self.email_textbox_id).clear()
        self.driver.find_element(By.ID, self.email_textbox_id).send_keys(email)

    def enter_password(self,password):
        self.driver.find_element(By.ID, self.password_textbox_id).clear()
        self.driver.find_element(By.ID, self.password_textbox_id).send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, self.login_button_xpath).click()

    def check_details(self):
        msg = self.driver.find_element(By.XPATH, self.dashboard_details_message_xpath).text
        return msg

    def check_invalid_credentials(self):
        msg = self.driver.find_element(By.XPATH, self.invalid_credentials_message_xpath).text
        return msg


