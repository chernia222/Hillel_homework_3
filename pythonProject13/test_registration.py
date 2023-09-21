import pytest
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver_close(request, driver):
    yield driver
    driver.close()


class TestBase:
    def setup_method(self):
        self._driver = webdriver.Chrome()
        self._session = requests.session()

    def teardown_method(self):
        self._driver.quit()


class TestRegistration(TestBase):
    def setup_class(self):
        self.user_email = "testLastName@test.com"
        self.user_password = "Qwerty987"

        self.user_to_login = {
            "email": self.user_email,
            "password": self.user_password,
            "remember": False
        }

    def teardown_method(self):
        print("CHILD")
        self._session.post(url="https://qauto2.forstudy.space/api/auth/signin", json=self.user_to_login)
        self._session.delete(url="https://qauto2.forstudy.space/api/users")

    def test_registration_test(self):
        self._driver.implicitly_wait(3)
        self._driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

        sign_up_button = self._driver.find_element(By.XPATH, "//button[text()='Sign up']")
        sign_up_button.click()

        name_input = self._driver.find_element(By.ID, "signupName")
        name_input.send_keys("Tester")

        last_name_input = self._driver.find_element(By.ID, "signupLastName")
        last_name_input.send_keys("testLastName")

        email_input = self._driver.find_element(By.ID, "signupEmail")
        email_input.send_keys(self.user_email)

        password_input = self._driver.find_element(By.ID, "signupPassword")
        password_input.send_keys(self.user_password)

        repeat_password_input = self._driver.find_element(By.ID, "signupRepeatPassword")
        repeat_password_input.send_keys(self.user_password)

        register_button = self._driver.find_element(By.XPATH, "//button[text()='Register']")
        register_button.click()

        empty_garage = self._driver.find_elements(By.XPATH, "//p[text()='You don't have any cars in your garage']")

        assert len(empty_garage) != 0
