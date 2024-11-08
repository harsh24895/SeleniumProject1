"""
This module contians duckduckGorulesPage
"""
# Ch-4 Defining page objects and ch-6
from selenium.webdriver.common.by import By

class DuckDuckGoResultPage:
    # Locators

    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
    SEARCH_INPUT = (By.ID, 'searchbox_input')

    # Initializer
    def __init__(self, browser):
        self.browser = browser

    # Interaction Methods
    # This will return the link titles of results
    def result_link_titles(self):
        links = self.browser.find_elements(*self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    # this will get the text value from the search input field from result page
    def search_input_value(self):
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title