import pytest

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage

#Chapter 9:Running tests in detail
# you run test in parallel we need to install following
# In here we need to install plugins: pipenv install pytest-xdist
# Now here we need to run specific three set for test as mention below in parameterize: pipenv run python -m pytest -n 3

@pytest.mark.parametrize('phrase',['panda','python','polar bear'])
def test_basic_duckduckgo_search(browser, phrase):

    search_page = DuckDuckGoSearchPage(browser)
    result_page = DuckDuckGoResultPage(browser)

    #give the duckduckgo home page
    search_page.load()

    #when the user searches for "panda"
    search_page.search(phrase)


    #and the search result query is "panda"
    assert phrase == result_page.search_input_value()

    #And the search result links pertain to "panda"
    #this code is updated below
    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

   #And the search result title contains "panda"
    assert phrase in result_page.title()