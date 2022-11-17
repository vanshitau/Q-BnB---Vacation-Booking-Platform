from qbay.models import (
    register
)

# Using readlines()
sqlfile = open('Generic_SQLI.txt', 'r')
Lines = sqlfile.readlines()

# Strips the newline character
def test_sql_register_id():
    for line in Lines:
        register(line, 'user0', 'test00@test.com', 'Abcdef!')

def test_sql_register_name():
    for line in Lines:
        register(21, line, 'test10@test.com', 'Abcdef!')

def test_sql_register_email():
    for line in Lines:
        register(22, 'user2', line, 'Abcdef!')

def test_sql_register_password():
    for line in Lines:
        register(23, 'user3', 'test30@test.com', line)