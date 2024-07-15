import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    Email_field_Name = "email"
    Password_field_Name = "password"
    Login_button_CSSSelector = "//button[@type='submit']"

    def click_into_email(self):
        time.sleep(2)
        self.driver.find_element(By.NAME, self.Email_field_Name).click()

    def input_into_email(self, email):
        time.sleep(2)
        self.driver.find_element(By.NAME, self.Email_field_Name).send_keys(email)
        self.driver.find_element(By.NAME, self.Email_field_Name).send_keys(Keys.ENTER)
        time.sleep(2)
    def click_into_password(self):
        time.sleep(2)
        self.driver.find_element(By.NAME, self.Password_field_Name).click()
        time.sleep(2)

    def input_into_password(self, password):
        self.driver.find_element(By.NAME, self.Password_field_Name).send_keys(password)
        time.sleep(5)
        self.driver.find_element(By.NAME, self.Password_field_Name).send_keys(Keys.ENTER)


