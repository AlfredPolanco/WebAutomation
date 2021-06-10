"""
Test case to validate google homepage elements
"""

import pytest
from pages.home_page import HomePage
import time

TEST_NAME = 'test_validate_home_icons'

# @pytest.mark.parametrize('test_name', [TEST_NAME])
def test_administrar_los_canales_de_venta_y_poder_crear_nuevos(web_driver):
    TEXT = 'Youtube'
    google_home_page = HomePage(web_driver)
    google_home_page.type_search_bar_input(TEXT)
    time.sleep(5)

