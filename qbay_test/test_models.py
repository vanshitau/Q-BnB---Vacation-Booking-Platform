from qbay.models import register, login, username_helper


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''
    # id, name, email, password, billing_address, postal_code, account_bal
    assert register('0', 'u0', 'test0@test.com', '123456', 'bill ave', 'L8K 2G2', '0') is True
    assert register('1', 'u0', 'test1@test.com', '123456', 'tommy st', 'J8Y 3R3', '100') is True
    assert register('2', 'u1', 'test0@test.com', '123456', 'sally st', 'M0P 2S5', '0') is False


def test_r2_1_login():
    '''
    Testing R2-1: A user can log in using her/his email address 
      and the password.
    (will be tested after the previous test, so we already have u0, 
      u1 in database)
    '''

    user = login('test0@test.com', 123456)
    assert user is not None
    assert user.username == 'u0'

    user = login('test0@test.com', 1234567)
    assert user is None


def test_r1_6_username_helper():
    '''
    Testing R1-6: User name has to be longer than 2 characters and 
    less than 20 characters.
    '''
    user = username_helper('u0')    # username is only 2 chars
    assert user is not None

    user = username_helper('testinglongerusername')   # username is over 20 chars
    assert user is None

