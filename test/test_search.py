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
def test_basic_duckduckgo(browser):

    #give the duckduckgo home page
    #TODO

    #when the user searchs for "panda"
    #TODo

    #then the search result title contains "panda"
    #TODO

    #and the search result query is "panda"
    #TODO

    #And the search result links pertain to "panda"
    #TODO

    raise Exception("Incomplete Test")