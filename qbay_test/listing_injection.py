from qbay.models import (listing, register, booked)
from datetime import datetime

# Using readlines()
file1 = open('Generic_SQLI.txt', 'r')
Lines = file1.readlines()

user = register(None, 'user0', 'test@test.com', 'Abcdef!')
buyer = register(None, 'user1', 'test1@test.com', 'Abcdef!')


def test_sql_listing_title():
    ''' Testing the title on the create listing page '''
    for line in Lines:
        listing(
            None, line, "My house this is a description", 100, user.id, 
            datetime(2024, 1, 5).strftime('%Y-%m-%d')
        )

     
def test_sql_listing_description():
    ''' Testing the description on the create listing page '''
    for line in Lines:
        listing(
            None, "title", line, 100, user.id, 
            datetime(2024, 1, 5).strftime('%Y-%m-%d')
        )  


def test_sql_listing_price():
    ''' Testing the price on the create listing page '''
    for line in Lines:
        listing(
            None, "title", "My house this is a description", line, user.id,
            datetime(2024, 1, 5).strftime('%Y-%m-%d')
        )  


def test_sql_booking_start_date():
    ''' Testing the start date on the create booking page '''
    for line in Lines:
        booked(
            user.id, buyer.id, line, 
            datetime(2024, 1, 5).strftime('%Y-%m-%d'),
        ) 
        

def test_sql_booking_end_date():
    ''' Testing the end date on the create booking page '''
    for line in Lines:
        booked(
            user.id, buyer.id, 
            datetime(2024, 1, 5).strftime('%Y-%m-%d'), line
        ) 

