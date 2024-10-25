#Setting up the selenium websriver chapter 3


#Setup the Chrome driver and geckodr
#Now we have to setup the chrome in system path or user path as per the project is working on
# currently i had added the chromr driver and geckodriver in User varaible under PATH
# You need to creata a folder in your user folder in C:\ and then add the path to the PATH in environment vairable
# then check both driver install correctly use:  chromedriver --version
#geckodriver --version

# Now we have to install selenium after that
# for selenium : pipenv install selenium


# here we are adding the fixture in the function
# as we have mention the fixture name in the function it will look for browser in the confest file


#here we have imported the page object classes
from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


def test_basic_duckduckgo_search(browser):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)
    PHRASE = "DuckDuckGo — Privacy, simplified." # Because of the css selector is looking for this text for test i'm mentioning this

    #give the duckduckgo home page
    search_page.load()

    #when the user searches for "panda"
    search_page.search(PHRASE)

    #then the search result title contains "panda"
    assert PHRASE in result_page.title()

    #and the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    #And the search result links pertain to "panda"
    #this code is updated below
    titles = result_page.result_link_titles()
    matches = [t for t in titles if PHRASE.lower() in t.lower()]
    assert len(matches) > 0

    #Remove the exception once the test is complete
    raise Exception("Incomplete Test")