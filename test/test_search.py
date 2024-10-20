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
from pages.result import DuckduckGoresultPage
from pages.search import DuckduckGoSearchPage

def test_basic_duckduckgo(browser):

    search_page = DuckduckGoSearchPage(browser)
    result_page = DuckduckGoresultPage(browser)
    PHRASE = "panda"

    #give the duckduckgo home page
    search_page.load()

    #when the user searchs for "panda"
    search_page.search(PHRASE)

    #then the search result title contains "panda"
    assert PHRASE in result_page.title()

    #and the search result query is "panda"
    assert PHRASE == result_page.search_input_value()

    #And the search result links pertain to "panda"
    for title in result_page.result_link_titles():
        assert  PHRASE.lower() in title.lower()

    #Remove the exception once the test is complete
    raise Exception("Incomplete Test")