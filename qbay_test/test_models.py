from datetime import datetime
from qbay.models import (register, check_price, check_date, title_desc, check_owner, login, update_listing, 
username_helper, postal_code_helper, update_user, email_helper, password_helper, user_id_helper, listing)

def test_r1_7_user_register():
  '''
  Testing R1-7: If the email has been used, the operation failed.
  '''
  user = register(1, 'user0', 'test0@test.com', 'Abcdef!')
  assert user is not None
  assert user.email == 'test0@test.com'
  user = register(2, 'user0', 'test1@test.com', 'Abcdef!')
  assert user is not None
  assert user.email == 'test1@test.com'
  user = register(3, 'user1', 'test0@test.com', 'Abcdef!')
  assert user is None

def test_r1_8_user_register():
  '''
  Testing R1-8: Shipping address is empty at the time of registration.
  '''
  user = register(1, 'user1', 'test@test.com', 'Abcdef!')
  assert user is not None
  assert user.billing_address == ''


def test_r2_1_2_login():
  '''
  Testing R2-1: A user can log in using her/his email address 
    and the password.
  (will be tested after the previous test, so we already have u0, 
    u1 in database)
  Testing R2-1: The email and password that are supplied as input
    must have the same requirements as the register function
  '''

  user = login('test0@test.com', 'Abcdef!')
  assert user is not None
  assert user.username == 'user0'

  user = login('test0@test.com', 'abcdef!')
  assert user is None


def test_r5_1_4_update_listing():
  '''
  Testing R5-1: Updating the title, description, and price of a listing
    depending on the listing id. The attributes that are not being changed 
    are passed into the function as none.
  Testing R5-4: The updated attributes follow the same requirements as when
    the listing was created
  '''
  listing(1, "house", "My house is very big you should stay here", 100, 1, datetime(2024,1,5))
  assert update_listing(1, "My House", None, None) is True
  assert update_listing(1, None, "This is my house", None) is True
  assert update_listing(1, None, None, 500) is True


def test_r4_1_to_4_title():
  '''
  Testing R4-1 and R4-2: A user can create a listing only if the title is alphanumeric and 
  if the title does not begin with a space
  '''
  #this should give true since all requirements are met
  assert title_desc("Condo for rent", "Two bedroom condo for rent in Downtown Toronto") is True
  #this should give false since the title has a leading space
  assert title_desc(" Condo for rent", "Two bedroom condo for rent in Downtown Toronto") is False
  #this should give false since the title has a trailing space
  assert title_desc("Condo for rent ", "Two bedroom condo for rent in Downtown Toronto") is False
  #this should give false since the title is not all alphanumeric
  assert title_desc("Condo for rent&", "Two bedroom condo for rent in Downtown Toronto") is False
  #this should give false since the description is shorter than the title length
  assert title_desc("Condo for rent", "Two bedroom") is False

def test_r4_5_price():
  '''
  Testing R4-5: The price of the listing must between 10 and 10,000
  '''
  #price should not be none since the price is between 10 and 10000
  price = check_price(2000)
  assert price is not None

  #price should be none since the price is not between 10 and 10000
  price = check_price(2)
  assert price is None
  

def test_r4_6_date():
  '''
  Testing R4-6: The date of the listing must between '2021-01-02' and '2025-01-02'
  '''
  #price should not be none since the price is between 10 and 10000
  date = check_date(datetime(2024,1,2))
  assert date is not None

  date = check_date(datetime(2019,1,2))
  assert date is None


def test_r4_7_owner():
  '''
  Testing R4-7: This will check to see if the user's email is not empty and make sure the user exists in the db
  '''

  user = login("test0@test.com", "Abcdef!")
  #should give true since there is an owner in the database with that email
  assert check_owner(user.id) is True
  #should give false since the email is empty
  user.email = ""
  assert check_owner(user.id) is False

def test_r5_2_price_change():
  '''
  Testing R5-2: The price can only ever be increased when it is updated, 
    never decreased. 
  '''
  assert update_listing(1, None, None, 500) is True #price of listing is 500
  assert update_listing(1, None, None, 50) is False #decreasing the price
  assert update_listing(1, None, None, 5000) is True #increasing the price


def test_r5_3_date_modified():
  '''
  Testing R5-3: When at least one attribute has been updated, the last 
    modified date of the file needs to be updated
  '''
  assert update_listing(1, "My House", None, None) is True
  assert update_listing(1, None, None, None) is True


def test_r1_9_user_register():
  '''
  Testing R1-9: Postal code is empty at the time of registration.
  '''
  user = register(3, 'user3', 'testemail@test.com', 'Abcdef!')
  assert user is not None
  assert user.postal_code == ''


def test_r1_10_user_register():
  '''
  Testing R1-10: Balance should be initialized as 100 at the time of registration. 
  (free $100 dollar signup bonus).
  '''
  user = register(4, 'user4', 'testEmail@test.com', 'Abcdef!')
  assert user is not None
  assert user.account_bal == 100


def test_r1_6_username_helper():
  '''
  Testing R1-6: User name has to be longer than 2 characters and 
  less than 20 characters.
  '''
  user = username_helper('user123')
  assert user is not None
  user = username_helper('testinglongerusername')
  assert user is None
  user = username_helper('Ab')
  assert user is None


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
  username = username_helper('abcdefg')
  assert username is not None
  username = username_helper('')
  assert username is None
  username = username_helper('1234')
  assert username is not None
  username = username_helper('  pass')
  assert username is None
  username = username_helper('1234!!!')
  assert username is not None

def test_r3_1_update():
  '''
  Testing P3-1: A user is only able to update his/her user name, user email, 
  billing address, and postal code
  '''
  assert update_user(1, "sally04", "sally04@gmail.com", "sally st", "F5Y 3B5") is True
  assert update_user(20, "sally04", "sally04@gmail.com", "sally st", "F5Y 3B5") is False

# def test_r3_1_update():
#   '''
#   Testing P3-1: A user is only able to update his/her user name, user email, 
#   billing address, and postal code
#   '''
#   user = update('user123', 'test0@test.com', 'john st', 'L5J2V2')
#   assert user is not None
#   assert user.username is 'user123'
#   assert user.email is 'test0@test.com'
#   assert user.billing_address is 'john st'
#   assert user.postal_code is 'L5J2V2'

def test_r1_1_register():
  '''
  Testing R1-1: Email cannot be empty. password cannot be empty.
  '''
  assert register(1,'jill1_123','jill_mitchell@outlook.com','') is None
  assert register(3,'jill3_123','','Good#1234') is None
  user = register(2,'jill2_123','jill_m@outlook.com','Good#1234')
  assert user is not None


def test_r1_2_user_id_helper():
  '''
  Testing R1-3:  The email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for 
  a human-friendly explanation). You can use external libraries/imports.
  '''

  assert user_id_helper('user0') is True
  assert user_id_helper('user1') is True
  assert user_id_helper('user2') is True
  

def test_r1_3_email_helper():
  '''
  Testing R1-3:  The email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for 
  a human-friendly explanation). You can use external libraries/imports.
  '''
  assert email_helper('sam_mitchell@outlook.com') is True
  assert email_helper('bob_m12@gmail.com') is True
  assert email_helper('bob.ross@gmail.com') is True
  assert email_helper('kenny-wright24@yahoo.com') is True
  assert email_helper('sam_mitchell@out.look.com') is False


def test_r1_4_password_helper():
  '''
  Testing R1-4: Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, 
  and at least one special character.
  '''
  assert password_helper("Queensuni.2024") is True
  assert password_helper('Queen#_1926') is True
  assert password_helper('brieR23') is False
  assert password_helper('brehi') is False
  assert password_helper('') is False


def test_r1_5_username_helper():
  '''
  Testing R1-5: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not as the prefix or suffix.
  '''
  username = username_helper('jasondawn123')
  assert username is not None
  username = username_helper('bob rawn')
  assert username is not None
  username = username_helper('john henry')
  assert username is not None
  username = username_helper(' huh-123')
  assert username is None
  username = username_helper('')
  assert username is None


def test_r3_2_postal_code_helper():
  '''
  Testing R3-2: postal code should be non-empty, alphanumeric-only, and no special characters such as !.
  '''
  assert postal_code_helper('K7L3D4') is True
  assert postal_code_helper('L553NN') is False
  assert postal_code_helper('ABC ') is False
  assert postal_code_helper('') is False
  assert postal_code_helper('T_45C3!') is False