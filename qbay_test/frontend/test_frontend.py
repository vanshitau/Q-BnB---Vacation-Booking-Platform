from seleniumbase import BaseCase

from qbay_test.conftest import base_url
from unittest.mock import patch
from qbay.models import User

"""
This file defines all integration tests for the frontend homepage.
"""


class FrontEndHomePageTest(BaseCase):

    def test_1_register_functaionality(self, *_):
        """
        This is a testing register functionality coverage.
        """
        # open register page
        self.open(base_url + '/register')
        
        # FUNC TESTING FOR NAME --- FAILS

        # testing empty name
        self.type("#email", "student@gmail.com")
        self.type("#name", "")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing alphanumeric name with special char
        self.type("#email", "student@gmail.com")
        self.type("#name", "Student!!!")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing prefix space name
        self.type("#email", "student@gmail.com")
        self.type("#name", "   Student")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing suffix space name
        self.type("#email", "student@gmail.com")
        self.type("#name", "Student   ")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing name too short
        self.type("#email", "student@gmail.com")
        self.type("#name", "S")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing name too long
        self.type("#email", "student@gmail.com")
        self.type("#name", "StudentStudentStudentStudent")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # FUNC TESTING FOR NAME --- SUCCESS

        # registering with valid email
        self.type("#email", "student@gmail.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!") 
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # logging in with valid email
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')
        
        # open home page (success)
        self.open(base_url)
        
    def test_2_register_input(self, *_):
        """
        This is a testing register input coverage.
        """
        # open register page
        self.open(base_url + '/register')
        
        # INPUT TESTING FOR EMAIL --- FAILS

        # testing empty email
        self.type("#email", "")
        self.type("#name", "Student")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing email format
        self.type("#email", "studentstudent.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # INPUT TESTING FOR EMAIL --- SUCCESS

        # registering with valid email
        self.type("#email", "student@gmail.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!") 
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # logging in with valid email
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')
        # open home page (success)
        self.open(base_url)

    def test_3_register_output_fail(self, *_):
        """
        This is a test for register output coverage.
        """
        # open register page
        self.open(base_url + '/register')

        # OUTPUT TESTING FOR PASSWORD --- FAIL

        # testing password2 matches password
        self.type("#email", "student@gmail.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!")
        self.type("#password2", "Student1?")
        # click enter button
        self.click('input[type="submit"]')
        # testing output (error message)
        self.assert_element("#message")
        self.assert_text("The passwords do not match", "#message")
    
    def test_4_register_output_success(self, *_):
        """
        This is a test for register output coverage.
        """
        # open register page
        self.open(base_url + '/register')

        # registering with valid email
        self.type("#email", "student1@gmail.com")
        self.type("#name", "Student1")
        self.type("#password", "Student1234!") 
        self.type("#password2", "Student1234!")
        # click enter button
        self.click('input[type="submit"]')

        # logging in with valid email
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student1@gmail.com")
        self.type("#password", "Student1234!")
        # click enter button
        self.click('input[type="submit"]')
        
        # open home page (success)
        self.open(base_url)
        # test if correct user name is displayed
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Student1 !", "#welcome-header")

    def test_5_login(self, *_):
        """
        This is testing login input coverage.
        """
        # open register page
        self.open(base_url + '/register')

        # login with valid email
        self.type("#email", "student@gmail.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!") 
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing empty email - fails
        self.type("#email", "")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing email format - fails
        self.type("#email", "studentstudent.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # login with invalid password - fail
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student") 
        # click enter button
        self.click('input[type="submit"]')

        # login with a valid password - pass
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!") 
        # click enter button
        self.click('input[type="submit"]')
        self.open(base_url)

    def test_6_update_listing_functionality(self, *_):
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

        self.open(base_url + '/update_listing/23')
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

    def test_7_create_listing_output(self, *_):

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # open update listing page
        self.open(base_url + '/update_listing/25')

        # this is unsucessful listing creation - price is invalid 
        self.type("#title", "Sucessful title")
        self.type("#description", "Thid description is also very valid hfhf")
        self.type("#price", 1)
        # click enter button
        self.click('input[type="submit"]')
        
        # confirm output is incorrect
        self.assert_element("#message")
        self.assert_text("Listing update failed.", "#message")

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
        self.assert_element("#product_25")
        self.assert_text("price: $200", "#product_25")

    def test_8_create_listing_input(self, *_):

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')
        
        # open create listing page
        self.open(base_url + '/update_listing/23')

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
    
    def test_9_updateUser_input(self, *_):
        # open register page
        self.open(base_url + '/register')
        # registering with valid email
        self.type("#email", "student@gmail.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!") 
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # logging in with valid email
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID postal code --> not the correct format
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student")
        self.type("#email", "student@gmail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "LAA2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID postal code --> empty
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student")
        self.type("#email", "student@gmail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "")
        # click enter button
        self.click('input[type="submit"]')

        # VALID
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student")
        self.type("#email", "student@gmail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # Check billing address

        # INVALID billing address --> empty
        self.open(base_url + '/updateUser')
        # fill username, email, billing address 
        # and postal code
        self.type("#username", "Student")
        self.type("#email", "student@gmail.com")
        self.type("#billing_address", "")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # VALID
        self.open(base_url + '/updateUser')
        # fill username, email, billing address 
        # and postal code
        self.type("#username", "Student")
        self.type("#email", "student@gmail.com")
        self.type("#billing_address", "1411 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # Open the home page
        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Student !", "#welcome-header")

    def test_10_updateUser_output(self, *_):
        # open register page
        self.open(base_url + '/register')
        # registering with valid email
        self.type("#email", "student@gmail.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!") 
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # logging in with valid email
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID username
        # The username is greater than 20 characters
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student123456789101122")
        self.type("#email", "student@gmail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID username
        # There is a space in the begining
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", " Student12")
        self.type("#email", "student@gmail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID username
        # The username has an "!" at the end --> not alphanumeric
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student!")
        self.type("#email", "student@gmail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # VALID username
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student1234")
        self.type("#email", "student@gmail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')
        
        # Open the home page
        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Student1234 !", "#welcome-header")

    def test_11_updateUser_functionality(self, *_):
        # open register page
        self.open(base_url + '/register')
        # registering with valid email
        self.type("#email", "student@gmail.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!") 
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')
        
        # Check email
        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')
        
        # INVALID email --> "_" in domain
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student")
        self.type("#email", "student@gm_ail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID email --> empty
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student")
        self.type("#email", "")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # INVALID email --> Email is has more than 3 letters after "." 
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student")
        self.type("#email", "student@gmail.come")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # VALID
        # open user update page
        self.open(base_url + '/updateUser')
        # fill username, email, billing address and postal code
        self.type("#username", "Student")
        self.type("#email", "student_1@gmail.com")
        self.type("#billing_address", "141 Courtney Street")
        self.type("#postal_code", "L7A2C6")
        # click enter button
        self.click('input[type="submit"]')

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student_1@gmail.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        self.open(base_url)
        self.assert_element("#welcome-header")
        self.assert_text("Welcome Student !", "#welcome-header")

    def test_12_create_listing_functionality(self, *_):
        """
        This is a sample front end unit test to login to home page
        and verify if the tickets are correctly listed.
        """
        # open register page
        self.open(base_url + '/register')
        # fill email and password
        self.type("#email", "student@student.com")
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
        self.type("#email", "student@student.com")
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

        # functionality testing for title - req. partioning
        # title has a leading space, description is fine, price is fine
        self.type("#title", " Leading space")
        self.type("#description", "My house is very big you should stay here")
        self.type("#price", 100)
        self.click('input[type="submit"]')

        # title has a trailing space, description is fine, price is fine
        self.type("#title", "Trailing space ")
        self.type("#description", "My house is very big you should stay here")
        self.type("#price", 100)
        # click enter button
        self.click('input[type="submit"]')

        # title is greater than 80 chars, description is fine, price is fine
        self.type(
            "#title", 
            "this title is way to long bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
            + "bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb"
        )
        self.type("#description", "My house is very big you should stay here")
        self.type("#price", 100)
        # click enter button
        self.click('input[type="submit"]')

        # title is not all alphanum., description is fine, price is fine
        self.type("#title", "Th!s title is n>t alphanum")
        self.type("#description", "My house is very big you should stay here")
        self.type("#price", 100)
        # click enter button
        self.click('input[type="submit"]')

        # title is fine, description is fine, price is fine - successful 
        self.type("#title", "Sucessful title")
        self.type("#description", "this description is valid and it passed")
        self.type("#price", 100)
        # click enter button
        self.click('input[type="submit"]')

    def test_13_create_listing_output(self, *_):

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@student.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')
    
        # open create listing page
        self.open(base_url + '/create_listing')

        # this is unsucessful listing creation - price is invalid 
        self.type("#title", "Sucessful title")
        self.type("#description", "Thid description is also very valid hfhf")
        self.type("#price", 1)
        # click enter button
        self.click('input[type="submit"]')
        
        # confirm output is incorrect
        self.assert_element("#message")
        self.assert_text("Price is not between 10 and 10000", "#message")

        # title is fine, description is fine, price is fine - successful 
        self.type("#title", "valid title")
        self.type(
            "#description", 
            "this description is valid and it passed beonvoernvv"
        )
        self.type("#price", 100)
        # click enter button
        self.click('input[type="submit"]')
        
        # open home page
        self.open(base_url)
        # output is correct - price is valid and showed on the home page
        self.assert_element("#product_24")
        self.assert_text("price: $100", "#product_24")

    def test_14_create_listing_input(self, *_):

        # open login page
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@student.com")
        self.type("#password", "Student123!")
        # click enter button
        self.click('input[type="submit"]')
        
        # open create listing page
        self.open(base_url + '/create_listing')

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

    def test_15_booked_listing_output(self, *_):
            # open register page
            self.open(base_url + '/register')
            # registering with valid email
            self.type("#email", "student@gmail.com")
            self.type("#name", "Student")
            self.type("#password", "Student123!") 
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

            # open create listing page
            self.open(base_url + '/create_listing')

            self.type("#title", "Sucessful")
            self.type("#description", "this description of the booked listing")
            self.type("#price", 10)
            # click enter button
            self.click('input[type="submit"]')

            # open update listing page
            self.open(base_url + '/create_booking')

            # this is sucessfully booked listing
            self.type("#listing_id", 1)
            self.type("#booked_start_date", "2023-05-12")
            self.type("#booked_end_date", "2023-06-12")

            # click enter button
            self.click('input[type="submit"]')
        
















    #     # confirm output is incorrect
    #     self.assert_element("#message")
    #     self.assert_text("Listing update failed.", "#message")

    #     # title is fine, description is fine, price is fine - successful 
    #     self.type("#title", "valid title")
    #     self.type(
    #         "#description", "this description is valid and it passed"
    #         + "nsfnsfsfusfs"
    #     )
    #     self.type("#price", 200)
    #     # click enter button
    #     self.click('input[type="submit"]')
        
    #     # open home page
    #     self.open(base_url)
    #     # output is correct - price is valid and showed on the home page
    #     self.assert_element("#product_25")
    #     self.assert_text("price: $200", "#product_25")

    # def test_8_create_listing_input(self, *_):

    #     # open login page
    #     self.open(base_url + '/login')
    #     # fill email and password
    #     self.type("#email", "student@gmail.com")
    #     self.type("#password", "Student123!")
    #     # click enter button
    #     self.click('input[type="submit"]')
        
    #     # open create listing page
    #     self.open(base_url + '/update_listing/23')

    #     # input testing for description 
    #     # desc is empty
    #     self.type("#title", "title")
    #     self.type("#description", "")
    #     self.type("#price", 100)
    #     self.click('input[type="submit"]')

    #     # desc is too short
    #     self.type("#title", "title")
    #     self.type("#description", "this is short")
    #     self.type("#price", 100)
    #     self.click('input[type="submit"]')

    #     # desc is shorter than title
    #     self.type("#title", "my title")
    #     self.type("#description", "short")
    #     self.type("#price", 100)
    #     self.click('input[type="submit"]')

    #     # desc is too long
    #     desc = "a" * 2001
    #     self.type("#title", "title")
    #     self.type("#description", desc)
    #     self.type("#price", 200)
    #     self.click('input[type="submit"]')

    #     # title is fine, description is fine, price is fine - successful 
    #     self.type("#title", "Sucessful title")
    #     self.type("#description", "this description is valid and it passed")
    #     self.type("#price", 100)
    #     # click enter button
    #     self.click('input[type="submit"]')
    