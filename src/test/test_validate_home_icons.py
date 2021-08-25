"""
Test case to validate google homepage elements
"""

from pages.home_page import HomePage
import time


TEST_NAME = 'test_validate_home_icons'

def test_administrar_los_canales_de_venta_y_poder_crear_nuevos(web_driver):
    TEXT = 'Youtube'
    google_home_page = HomePage(web_driver)
    time.sleep(10)
    google_home_page.click_login_button()
    time.sleep(500)
    # google_home_page.type_search_bar_input(TEXT)
    # time.sleep(10)

