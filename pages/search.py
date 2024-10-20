"""
module contains DuckduckgoSearchpage,
the page object for the duckduckgo
"""
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class DuckduckGoSearchPage:

    #url
    URL = 'https://www.duckduckgo.com'

    #locators
    SEARCH_INPUT = (By.ID,'search_form_input_newtab')

    #initializer
    def __init__(self, browser):
        self.browser = browser

    #Interaction methods
    #this will load the webpage
    def load(self):
        self.browser.get(self.URL)


    def search(self,phrase):
        # * is a standard python thing and passing this we add the tuple which is next to it easily
        search_input = self.browser.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(phrase + Keys.RETURN)
