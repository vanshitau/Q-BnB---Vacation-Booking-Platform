from qbay.models import register

# open text file
file = open('Generic_SQLI.txt', 'r')
# read lines to file and assign to a variable
Lines = file.readlines()


def test_sql_register_name():
    '''
    Testing the username parameter on the register page.
    '''
    # go through each line in the file
    for line in Lines:
        # call the register function and pass in the line of code
        register(21, line, 'test10@test.com', 'Abcdef!')


def test_sql_register_email():
    '''
    Testing the email parameter on the register page.
    '''
    # go through each line in the file
    for line in Lines:
        # call the register function and pass in the line of code
        register(22, 'user2', line, 'Abcdef!')


def test_sql_register_password():
    '''
    Testing the password parameter on the register page. 
    '''
    # go through each line in the file
    for line in Lines:
        # call the register function and pass in the line of code
        register(23, 'user3', 'test30@test.com', line)