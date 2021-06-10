import pytest
from selenium import webdriver as selenium_web_driver

WAIT_TIME = 10
URL = 'https://www.google.com/'

@pytest.fixture(scope='session')
def config_wait_time():
    return WAIT_TIME

@pytest.fixture(scope='session')
def url():
    return URL

@pytest.fixture(scope='function')
def web_driver(config_wait_time):
    driver = selenium_web_driver.Chrome()

    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()

    yield driver

    driver.quit()