from qbay.models import (listing, register)
from datetime import datetime

# Using readlines()
file1 = open('Generic_SQLI.txt', 'r')
Lines = file1.readlines()

user = register(None, 'user0', 'test@test.com', 'Abcdef!')

def test_sql_listing_title():
    for line in Lines:
        listing1 = listing(None, line, "My house this is a description", 100, user.id,
            datetime(2024, 1, 5).strftime('%Y-%m-%d')
        )
        
def test_sql_listing_description():
    for line in Lines:
        listing2 = listing(None, "title", line, 100, user.id,
            datetime(2024, 1, 5).strftime('%Y-%m-%d')
        )   

def test_sql_listing_price():
    for line in Lines:
        listing3 = listing(None, "title", "My house this is a description", line, user.id,
            datetime(2024, 1, 5).strftime('%Y-%m-%d')
        )   