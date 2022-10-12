from qbay.models import register, login, username_helper, postal_code_helper, update

def test_r1_7_user_register():
  '''
  Testing R1-7: If the email has been used, the operation failed.
  '''
  assert register('user0', 'test0@test.com', '123456') is True
  assert register('user0', 'test1@test.com', '123456') is True
  assert register('user1', 'test0@test.com', '123456') is False


def test_r1_8_user_register():
  '''
  Testing R1-8: Shipping address is empty at the time of registration.
  '''
  user = register('user1', 'test@test.com', 'Abcdef123!')
  assert user is not None
  assert user.billing_address is ''


def test_r1_9_user_register():
  '''
  Testing R1-9: Postal code is empty at the time of registration.
  '''
  user = register('user1', 'test@test.com', 'Abcdef123!')
  assert user is not None
  assert user.postal_code is ''


def test_r1_10_user_register():
  '''
  Testing R1-10: Balance should be initialized as 100 at the time of registration. 
  (free $100 dollar signup bonus).
  '''
  user = register('user1', 'test@test.com', 'Abcdef123!')
  assert user is not None
  assert user.account_bal == 100


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
  assert username_helper('user123') is True
  assert username_helper('testinglongerusername') is False
  assert username_helper('Ab') is False


def test_r3_3_postal_code_helper():
  '''
  Testing P3-2: Postal code should be non-empty, alphanumeric-only, and 
  no special characters such as !.
  Testing R3-3: Postal code has to be a valid Canadian postal code.
  '''
  assert postal_code_helper('K7L3D4') is True
  assert postal_code_helper('L553NN') is False
  assert postal_code_helper('ABC ') is False
  assert postal_code_helper('') is False
  assert postal_code_helper('T_45C3!') is False


def test_r3_4_username_helper():
  '''
  Testing R3-4: User name follows the requirements above.
  (postal code should be non-empty, alphanumeric-only, and no special characters such as !)
  '''
  assert username_helper('abcdefg') is True
  assert username_helper('') is False
  assert username_helper('1234') is True
  assert username_helper('  pass') is False
  assert username_helper('1234!!!') is False


def test_r3_1_update():
  '''
  Testing P3-1: A user is only able to update his/her user name, user email, 
  billing address, and postal code
  '''
  user = update('user123', 'test0@test.com', 'john st', 'L5J2V2')
  assert user is not None
  assert user.username is 'user123'
  assert user.email is 'test0@test.com'
  assert user.billing_address is 'john st'
  assert user.postal_code is 'L5J2V2'