"""import time

import pytest
import self as self
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pages.PackageCreationPage import PackageCreationPage


@pytest.mark.usefixtures('setup_and_teardown')
class TestPackageCreate:
    def test_for_create_tour_package(self):
        package_create_page = PackageCreationPage(self.driver)
        package_create_page.click_into_package_submodule()
        time.sleep(40)
        "package_create_page.click_into_create_button()"""