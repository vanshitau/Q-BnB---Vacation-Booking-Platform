from qbay.models import register, login, update_listing


def test_r1_7_user_register():
    '''
    Testing R1-7: If the email has been used, the operation failed.
    '''

    assert register('u0', 'test0@test.com', 'Password!') is True
    assert register('u0', 'test1@test.com', 'Password!') is True
    assert register('u1', 'test0@test.com', 'Password!') is False


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
    assert user.username == 'u0'

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