import pytest
from selenium import webdriver as selenium_web_driver

WAIT_TIME = 10
URL = 'https://www.google.com/'

@pytest.fixture(scope='function')
def web_driver(WAIT_TIME):
    driver = selenium_web_driver.Chrome()

    driver.implicitly_wait(WAIT_TIME)
    driver.maximize_window()

    yield driver

    driver.quit()