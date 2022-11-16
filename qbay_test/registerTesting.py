from qbay.models import (
    register
)

# Using readlines()
sqlfile = open('Generic_SQLI.txt', 'r')
Lines = sqlfile.readlines()

# Strips the newline character
def test_sql_register_id():
    for line in Lines:
        user = register(line, 'user01', 'testing0@test.com', 'Abcdef!')
        assert user is not None

def test_sql_register_name():
    for line in Lines:
        user = register(20, line, 'tester0@test.com', 'Abcdef!')
        assert user is not None

def test_sql_register_email():
    pass

def test_sql_register_password():
    pass