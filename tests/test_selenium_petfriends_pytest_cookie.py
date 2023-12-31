from pages.petfriends import MainPage


def test_petfriends(web_driver):
    """ Authorize to Petfriends via cookies and create a screenshot when the login page is successful. """

    page = MainPage(web_driver)
    page.scroll_down()
    page.go_to_all_pets_page()  # Navigate to the all pets page after adding cookies
    # Make the screenshot of browser window:
    page._web_driver.save_screenshot('petfriends.png')

    # Close the web driver
    web_driver.quit()
