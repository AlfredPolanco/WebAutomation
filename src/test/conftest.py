import pytest

@pytest.fixture(scope='function')
def web_driver(web_driver, url):
    web_driver.get(url)

    yield web_driver



    web_driver.quit()