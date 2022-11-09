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
        self.type("#email", "student@student.com")
        self.type("#name", "")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing alphanumeric name with special char
        self.type("#email", "student@student.com")
        self.type("#name", "Student!!!")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing prefix space name
        self.type("#email", "student@student.com")
        self.type("#name", " Student")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing suffix space name
        self.type("#email", "student@student.com")
        self.type("#name", "Student ")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing name too short
        self.type("#email", "student@student.com")
        self.type("#name", "S")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # testing name too long
        self.type("#email", "student@student.com")
        self.type("#name", "StudentStudentStudentStudent")
        self.type("#password", "Student123!")
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

       
        # FUNC TESTING FOR NAME --- SUCCESS

        # registering with valid email
        self.type("#email", "student@student.com")
        self.type("#name", "Student 1")
        self.type("#password", "Student123!") 
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # logging in with valid email
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@student.com")
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
        self.type("#email", "student@student.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!") 
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # logging in with valid email
        self.open(base_url + '/login')
        # fill email and password
        self.type("#email", "student@student.com")
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
        self.type("#email", "student@student.com")
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

        # OUTPUT TESTING FOR REGISTER --- SUCCESS

        # registering with valid email
        self.type("#email", "student@student.com")
        self.type("#name", "Student")
        self.type("#password", "Student123!") 
        self.type("#password2", "Student123!")
        # click enter button
        self.click('input[type="submit"]')

        # logging in with valid email
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