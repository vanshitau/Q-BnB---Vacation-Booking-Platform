from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):

    def test1_update_listing_functionality(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "student@gmail.com")
        # CORRECT NAME
        self.type("#name", "Student")
        # CORRECT PASSWORD
        self.type("#password", "Student123!") 
        # CORRECT PASSWORD2
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # open home page (success)
        self.open(base_url)
        # test if correct user name is displayed
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Student !", "#welcome-header")

        # open create listing page
        self.open(base_url + '/create_listing')

        self.type("#title", "houses")
        self.type("#description", "My house is very big you should stay here")
        self.type("#price", 100)
        self.click('input[type="submit"]')

        self.open(base_url + '/update_listing/28')
        # functionality testing for title - req. partioning
        # title has a leading space, description is fine, price is fine
        self.type("#title", " Leading space")
        self.type("#description", "My house is very big you should stay here")
        self.type("#price", 101)
        self.click('input[type="submit"]')

        # title has a trailing space, description is fine, price is fine
        self.type("#title", "Trailing space ")
        self.type("#description", "My house is very big you should stay here")
        self.type("#price", 102)
        # click enter button
        self.click('input[type="submit"]')

        # title is greater than 80 chars, description is fine, price is fine
        self.type(
            "#title", 
            "this title is way to long bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
            + "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        )
        self.type("#description", "My house is very big you should stay here")
        self.type("#price", 103)
        # click enter button
        self.click('input[type="submit"]')

        # title is not all alphanum., description is fine, price is fine
        self.type("#title", "Th!s title is n>t alphanum")
        self.type("#description", "My house is very big you should stay here")
        self.type("#price", 104)
        # click enter button
        self.click('input[type="submit"]')

        # title is fine, description is fine, price is fine - successful 
        self.type("#title", "Sucessful title")
        self.type("#description", "this description is valid and it passed")
        self.type("#price", 105)
        # click enter button
        self.click('input[type="submit"]')

    def test2_create_listing_output(self, *_):

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')
    
        # open update listing page
        self.open(base_url + '/update_listing/28')

        # this is unsucessful listing creation - price is invalid 
        self.type("#title", "Sucessful title")
        self.type("#description", "Thid description is also very valid hfhf")
        self.type("#price", 1)
        # click enter button
        self.click('input[type="submit"]')
        
        # confirm output is incorrect
        self.assert_element("#message")
        self.assert_text("The price cannot be less than 10.", "#message")

        # title is fine, description is fine, price is fine - successful 
        self.type("#title", "valid title")
        self.type(
            "#description", "this description is valid and it passed"
            + "nsfnsfsfusfs"
        )
        self.type("#price", 200)
        # click enter button
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)
        # output is correct - price is valid and showed on the home page
        self.assert_element("#product_28")
        self.assert_text("price: $200", "#product_28")

    def test3_create_listing_input(self, *_):

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')
        
        # open create listing page
        self.open(base_url + '/update_listing/28')

        # input testing for description 
        # desc is empty
        self.type("#title", "title")
        self.type("#description", "")
        self.type("#price", 100)
        self.click('input[type="submit"]')

        # desc is too short
        self.type("#title", "title")
        self.type("#description", "this is short")
        self.type("#price", 100)
        self.click('input[type="submit"]')

        # desc is shorter than title
        self.type("#title", "my title")
        self.type("#description", "short")
        self.type("#price", 100)
        self.click('input[type="submit"]')

        # desc is too long
        desc = "a" * 2001
        self.type("#title", "title")
        self.type("#description", desc)
        self.type("#price", 200)
        self.click('input[type="submit"]')

        # title is fine, description is fine, price is fine - successful 
        self.type("#title", "Sucessful title")
        self.type("#description", "this description is valid and it passed")
        self.type("#price", 100)
        # click enter button
        self.click('input[type="submit"]')
