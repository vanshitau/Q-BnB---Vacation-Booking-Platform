from qbay.models import register, login, email_helper, password_helper, username_helper, postal_code_helper


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', '123456') is True
    assert register('u0', 'test1@test.com', '123456') is True
    assert register('u1', 'test0@test.com', '123456') is False


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

def test_r1_1_register():
 '''
  Testing R1-1: Email cannot be empty. password cannot be empty.
  '''

assert register('', 'jill_mitchell@outlook.com', '') is True

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
   Testing R1-5: User name has to be non-empty, alphanumeric-only, and space allowed only if it is not as the prefix or suffix.
   '''

   assert postal_code_helper('K7L3D4') is True
   assert postal_code_helper('L553NN') is False
   assert postal_code_helper('ABC ') is False
   assert postal_code_helper('') is False
   assert postal_code_helper('T_45C3!') is False
  


  
