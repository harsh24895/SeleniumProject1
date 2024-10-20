"""
This module contians duckduckGorulesPage
"""

from selenium.webdriver.common.by import By

class DuckduckGoresultPage:

    #locators
    Result_links = (By.CSS_SELECTOR, 'a.result__a ')
    SEARCH_INPUT = (By.ID, 'search_form_input_newtab')

    #initizlizer
    def __int__(self, browser):
        self.browser = browser

    #interaction methods
    # This will return the link titles of results
    def result_link_titles(self):
        links  = self.browser.find_elements(*self.Result_links)
        #we are getting the specific text here
        titles = [link.text for link in links]
        return titles

    #this will get the text value from the search input field from result page
    def search_input_value(self):
        search_input = self.browser.find_elements(*self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title