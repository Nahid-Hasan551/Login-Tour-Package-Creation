from Utilities import ReadConfigurations
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

driver_chrome = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))


@pytest.fixture()
def setup_and_teardown(request, driver=None):
    browser = ReadConfigurations.read_configuration("basic info", "browser")

    driver = None
    if browser.__eq__("chrome"):
        driver = webdriver.Chrome()
    elif browser.__eq__("firefox"):
        driver = webdriver.Firefox()
    elif browser.__eq__("edge"):
        driver = webdriver.Edge()
    else:
        print("Provide a valid browser name from this list chrome,firefox,edge")
    driver.maximize_window()
    application_url = ReadConfigurations.read_configuration("basic info", "url")
    driver.get(application_url)
    request.cls.driver = driver

