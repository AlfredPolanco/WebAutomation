import pytest
from selenium import webdriver as selenium_web_driver

from selenium_stealth import stealth

WAIT_TIME = 10
URL = 'https://gbhqatest.firebaseapp.com/'

@pytest.fixture(scope='session')
def config_wait_time():
    return WAIT_TIME

@pytest.fixture(scope='session')
def url():
    return URL

@pytest.fixture(scope='function')
def web_driver(config_wait_time):
    # driver = selenium_web_driver.Chrome()
    options = selenium_web_driver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)
    options.add_argument('--disable-blink-features=AutomationControlled')
    driver = selenium_web_driver.Chrome(options=options)
    stealth(driver,
            languages=["en-US", "en"],
            vendor="Google Inc.",
            platform="Win32",
            webgl_vendor="Intel Inc.",
            renderer="Intel Iris OpenGL Engine",
            fix_hairline=True,
        )

    driver.implicitly_wait(config_wait_time)
    driver.maximize_window()

    yield driver

    driver.quit()