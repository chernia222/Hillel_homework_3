#//header//button[@class='btn btn-outline-white header_signin']
#//header//button[text()='Sign In']
#//button[contains(text(), 'Sign ')]

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://guest:welcome2qauto@qauto2.forstudy.space/")

sign_up_button = driver.find_element(By.XPATH, "//button[text()='Sign up']")
sign_up_button.click()

name_field = driver.find_element(By.ID, "signupName")
name_field.send_keys("Tester")

signup_field = driver.find_element(By.ID, "signupLastName")
signup_field.send_keys("testLastName")

signup_email_field = driver.find_element(By.ID, "signupEmail")
signup_email_field.send_keys("testLastName@test.com")

signup_password_field = driver.find_element(By.ID, "signupPassword")
signup_password_field.send_keys("Qwerty987")

signup_repeat_password_field = driver.find_element(By.ID, "signupRepeatPassword")
signup_repeat_password_field.send_keys("Qwerty987")

register_button = driver.find_element(By.XPATH, "//button[text()='Register']")
register_button.click()

alert_text = driver.find_element(By.XPATH, "count(//h3[@class='panel-empty_message']/text()) > 1")



