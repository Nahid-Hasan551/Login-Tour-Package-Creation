import time

import none
import self
from selenium.common import NoAlertPresentException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert


class AlertHandler:
    def __init__(self, driver):
        self.driver = driver

    def dismiss_alert(self):
        try:
            alert = Alert(self.driver)
            alert.dismiss()
        except NoAlertPresentException:
            print("No alert present")


class PackageCreationPage:
    def __init__(self, driver):
        self.driver = driver

    dropdown_Xpath = '// *[ @ id = "val-modules"]'
    dropdown1_Xpath = '//*[@id="val-services"]'
    service_tour_by_Xpath = '//*[@id="val-modules"]/option[9]'
    admin_by_Xpath = '//*[@id="val-services"]/option[1]'

    def click_dropdown(self):
        self.driver.find_element(By.XPATH, self.dropdown_Xpath).click()

    def click_dropdown1(self):
        self.driver.find_element(By.XPATH, self.dropdown1_Xpath).click()

    def select_tour(self):
        self.driver.find_element(By.XPATH, self.service_tour_by_Xpath).click()

    def select_admin(self):
        self.driver.find_element(By.XPATH, self.admin_by_Xpath).click()
