import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
options.add_experimental_option("detach", True)


@pytest.fixture(scope="class")
def init_driver(request):
    supported_browsers = ["chrome", "firefox"]
    browser = os.environ.get('BROWSER', None)
    if not browser:
        raise Exception("The environment variable 'BROWSER' is not set.")
    browser = browser.lower()
    if browser not in supported_browsers:
        raise Exception(f"Provided browser '{browser}' not supported."
                        f"Supported are: {supported_browsers}")
    if browser in ('chrome'):
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    if browser in ('firefox'):
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
    request.cls.driver = driver
    yield driver
