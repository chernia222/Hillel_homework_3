from selenium.webdriver.common.by import By
from locators import RegistrationLocators

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    def sign_up(self):
        sign_up_button = self.driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()

    def fill_registration_form(self, name, last_name, email, password, repeat_password):
        self.driver.find_element(By.ID, RegistrationLocators.NAME_FIELD).send_keys(name)
        self.driver.find_element(By.ID, RegistrationLocators.LAST_NAME_FIELD).send_keys(last_name)
        self.driver.find_element(By.ID, RegistrationLocators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(By.ID, RegistrationLocators.PASSWORD_FIELD).send_keys(password)
        self.driver.find_element(By.ID, RegistrationLocators.REPEAT_PASSWORD_FIELD).send_keys(repeat_password)

    def register(self):
        register_button = self.driver.find_element(By.XPATH, "//button[text()='Register']")
        register_button.click()

    def get_alert_text(self):
        return self.driver.find_element(By.XPATH, "//h3[@class='panel-empty_message']").text
