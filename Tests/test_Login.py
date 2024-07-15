import time

import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


from pages.LoginPage import LoginPage


@pytest.mark.usefixtures('setup_and_teardown')
class TestLogin:
    def test_for_login(self):
        login_page = LoginPage(self.driver)

        login_page.click_into_email()
        login_page.input_into_email("qateam@gmail.com")
        login_page.click_into_password()
        login_page.input_into_password("Qa@team789")




