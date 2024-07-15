import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


class PackageCreationPage:
    def __init__(self, driver):
        self.driver = driver

    package_submodule_by_CSSSELECTOR = ".Package"
    create_button_by_Xpath = "btn btn-secondary"

    def click_into_package_submodule(self):
        self.driver.find_element(By.CSS_SELECTOR, self.package_submodule_by_CSSSELECTOR).click()

    """def click_into_create_button(self):
        self.driver.find_element(By.CLASS_NAME, self.create_button_by_Xpath).click()"""


