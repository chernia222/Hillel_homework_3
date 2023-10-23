from selenium import webdriver
from webdriver_utils import init_driver
from registration_page import RegistrationPage

def main15():
    driver = init_driver()
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

    registration_page = RegistrationPage(driver)
    registration_page.sign_up()
    registration_page.fill_registration_form("Tester", "testLastName", "testLastName@test.com", "Qwerty987", "Qwerty987")
    registration_page.register()

    alert_text = registration_page.get_alert_text()
    print(alert_text)

if __name__ == "__main15__":
    main15()