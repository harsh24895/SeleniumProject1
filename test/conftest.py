# For pytest fixture() have the setup and cleanup phase bydefault in it
# And it belongs to a special file called conftest.py which we have created now


import pytest
import selenium.webdriver


# here we have setting the decorater called fixture for the browser function
@pytest.fixture
def browser():
    # Intitialize the ChromeDriver instance
    b = selenium.webdriver.Chrome()

    # Make its call wait up to 10seconds for the element to appear
    b.implicitly_wait(10)

    # Return the webdriver instance for the setup
    # till here we are do with setup phase
    yield b

    # here we have start the cleanup phase
    # Quit the webdriver instance for the cleanup
    b.quit()
