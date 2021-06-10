"""
This module contains google home page elements
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class HomePage:

    def __init__(self, browser):
        self.browser = browser
        self.wait = WebDriverWait(browser, 120)

    @classmethod
    def search_bar_input(cls):
        return (By.XPATH, '//input[@type="text"]')

    @classmethod
    def buttons_input(cls):
        return (By.XPATH, '//input[@type="submit"]')

    #! Actions
    def type_search_bar_input(self, search):
        """
        Writes text to search bar

        Arguments
        ---------
        search: (str)
            Text to be searched
        """
        search_input = self.browser.find_element(*self.search_bar_input())
        search_input.send_keys(search)

    def click_search_button(self):
        """
        Click search button
        """
        click_search = self.browser.find_elements(*self.buttons_input())
        click_search[3].send_keys()
