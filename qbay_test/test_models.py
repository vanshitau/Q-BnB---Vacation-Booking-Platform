from qbay.models import (register, check_price, check_date, title_desc, check_owner, login, update_listing, 
username_helper, postal_code_helper, update, email_helper, password_helper, user_id_helper)

def test_r1_7_user_register():
  '''
  Testing R1-7: If the email has been used, the operation failed.
  '''
  user = register(1, 'user0', 'test0@test.com', 'Abcdef!')
  assert user is not None
  assert user.email == 'test0@test.com'
  user = register(1, 'user0', 'test1@test.com', 'Abcdef!')
  assert user is not None
  assert user.email == 'test1@test.com'
  user = register(1, 'user1', 'test0@test.com', 'Abcdef!')
  assert user is not None
  assert user.email == 'test0@test.com'

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

  user = login('test0@test.com', 'Password!')
  assert user is not None
  assert user.username == 'user0'

  user = login('test0@test.com', 'password!')
  assert user is None


def test_r5_1_4_update_listing():
  '''
  Testing R5-1: Updating the title, description, and price of a listing
    depending on the listing id. The attributes that are not being changed 
    are passed into the function as none.
  Testing R5-4: The updated attributes follow the same requirements as when
    the listing was created
  '''
  listing = update_listing(1, "My House", None, None)
  assert listing is not None
  assert listing.listing_id == 1
  assert listing.title == "My House"
  
  listing = update_listing(1, None, "This is my house", None)
  assert listing is not None
  assert listing.listing_id == 1
  assert listing.description == "This is my house"

  listing = update_listing(1, None, None, 500)
  assert listing is not None
  assert listing.listing_id == 1
  assert listing.price == 500


def test_r4_1_to_4_title():
  '''
  Testing R4-1 and R4-2: A user can create a listing only if the title is alphanumeric and 
  if the title does not begin with a space
  '''
  assert title_desc(1,"Condo for rent","Two Bedroom house located in center of downtown Toronto", 1000, '2022-01-02',123456) is True
  assert title_desc(1,"Apartment for rent","Two Bedroom house located in center of downtown Toronto", 1000, '2022-01-02',123456) is True
  assert title_desc(1,"Condo for rent","Two", 1000, '2022-01-02',123456) is False


def test_r4_5_price():
  '''
  Testing R4-5: The price of the listing must between 10 and 10,000
  '''
  price = check_price(2000)
  assert price is not None

  price = check_price(2)
  assert price is None
  

def test_r4_6_date():
  '''
  Testing R4-6: The date of the listing must between 2021-01-02' and '2025-01-02
  '''
  date = check_date('2024-01-05')
  assert date is not None

  date = check_date('2019-01-05')
  assert date is None


def test_r4_7_owner():
  '''
  Testing R4-7: This will check to see if the user's email is not empty and make sure the user exists in the db
  '''
  #should give false since there is no owner in the database with that id
  assert check_owner('test0@test.com', 202019) is False
  #should give true since there is an owner in the database with that id
  assert check_owner('test0@test.com', 202019) is True


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
  user = register(1, 'user1', 'test@test.com', 'Abcdef123!')
  assert user is not None
  assert user.postal_code is ''


def test_r1_10_user_register():
  '''
  Testing R1-10: Balance should be initialized as 100 at the time of registration. 
  (free $100 dollar signup bonus).
  '''
  user = register(1, 'user1', 'test@test.com', 'Abcdef123!')
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


def test_r1_1_register():
  '''
  Testing R1-1: Email cannot be empty. password cannot be empty.
  '''
  assert register(1, '', 'jill_mitchell@outlook.com', '') is True


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
  assert username_helper('jasondawn123') is True
  assert username_helper('bob rawn') is True
  assert username_helper('john henry') is True
  assert username_helper(' huh-123') is False
  assert username_helper('') is False


def test_r3_2_postal_code_helper():
  '''
  Testing R3-2: postal code should be non-empty, alphanumeric-only, and no special characters such as !.
  '''
  assert postal_code_helper('K7L3D4') is True
  assert postal_code_helper('L553NN') is False
  assert postal_code_helper('ABC ') is False
  assert postal_code_helper('') is False
  assert postal_code_helper('T_45C3!') is False
  


  
