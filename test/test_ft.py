#Steps to do for the setup
#install dependency first: pip install pipenv in terminal
#2. then mention : pipenv install
# this will create a virtual environment and good to create this environment for every project
#so that we can manage the dependecy locally

# Here if want to run the specific file go into specific folder in terminal ex:C:\Users\Harsh\PycharmProjects\SeleniumWebDriver\.venv\tests  and then run this command:  pipenv run python -m pytest
# and this should pass the test

import pytest
def test_the_testschr():
    assert True
