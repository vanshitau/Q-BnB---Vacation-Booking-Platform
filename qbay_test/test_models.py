from qbay.models import register, login, check_price, check_date, title_desc, check_owner

def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register(1, 'u0', 'test0@test.com', '123456') is True
    assert register( 2, 'u0', 'test1@test.com', '123456') is True
    assert register( 3, 'u1', 'test0@test.com', '123456') is False


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

 
  

   
    

  