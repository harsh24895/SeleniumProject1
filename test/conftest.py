# For pytest fixture() have the setup and cleanup phase bydefault in it
# And it belongs to a special file called conftest.py which we have created now

import json
import pytest
import selenium.webdriver

#Chapter 7: Configuring Multiple browser
# new fixture
@pytest.fixture
def config(scope='session'):
    #Read the file
    with open('config.json') as config_file:
        config = json.load(config_file)

    #assert values are acceptable
    assert config['browser'] in ['Firefox','Chrome','Headless Chrome']
    assert isinstance(config['implicit_wait'],int)
    assert config['implicit_wait'] > 0

    #Return config so it can be used
    return config

# here we have setting the decorater called fixture for the browser function
@pytest.fixture
def browser(config):
    #initialize the Webdriver instance
    if config['browser'] == 'Firefox':
        b = selenium.webdriver.Firefox()
    elif config['browser'] == 'Chrome':
        b = selenium.webdriver.Chrome()
    elif config['browser'] == 'Headless Chrome':
        opts = selenium.webdriver.ChromeOptions()
        opts.add_argument('headless')
        b = selenium.webdriver.Chrome(options=opts)
    else:
        raise Exception(f'Browser"{config["browser"]}" is not supported')


    #make its calls wait for elements to appear
    b.implicitly_wait(config['ímplicit_wait'])


    """ # Intitialize the ChromeDriver instance
    b = selenium.webdriver.Chrome()
    # Make its call wait up to 10seconds for the element to appear
    b.implicitly_wait(10)"""

    # Return the webdriver instance for the setup
    # till here we are do with setup phase
    yield b

    # here we have start the cleanup phase
    # Quit the webdriver instance for the cleanup
    b.quit()
