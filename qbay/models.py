from genericpath import exists
from sqlalchemy import PrimaryKeyConstraint
from qbay import app
from flask_sqlalchemy import SQLAlchemy
# from entities import *
from curses.ascii import isalnum, isalpha
#  from xxlimited import new
# import library to work with the current date
from datetime import *
import string
import re
import random
from sqlalchemy import func


'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)


class User(db.Model):
    '''
    R1-8
        Shipping address is empty at the time of registration.
    R1-9
        Postal code is empty at the time of registration.
    R1-10
        Balance should be initialized as 100 at the time of registration. 
        (free $100 dollar signup bonus).
    '''
    id = db.Column(
        db.Integer(), nullable=False, 
        autoincrement=True, primary_key=True
    )
    # added default value for billing_address = ""
    billing_address = db.Column(db.String(150), default="", nullable=False)
    # added default value of account_bal = 100
    account_bal = db.Column(db.Integer, default=100, nullable=False)
    # added default value of postal_code = ""
    postal_code = db.Column(db.String(20), default="", nullable=False)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class Listing(db.Model):
    '''
    Initiates the listing class and all of the columns of the listing
    '''
    id = db.Column(
        db.Integer, nullable=False, 
        primary_key=True, autoincrement=True
    )
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    last_modified_date = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<Listing %r>' % self.id


# create all tables
db.create_all()


def register(id, name, email, password):
    '''
    R1-7
        If the email has been used, the operation failed.
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
        billing_address (string): user billing address
        postal_code (string): user postal_code
        account_bal (integer): user account_bal
      Returns:
        True if registration succeeded otherwise False
    '''

    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return None

    existed = User.query.filter_by(id=id).all()
    if len(existed) > 0:
        return None
    # check input meets the requirements
    if (
        username_helper(name) is False or password_helper(password) is False 
        or email_helper(email) is False
    ):
        return None
    else:
        # r1_2  
        if id is not None:
            # create a new user
            user = User(id=id, username=name, email=email, password=password)
        else:
            max_id = db.session.query(func.max(User.id)).scalar()
            if max_id is None:
                max_id = 0
            next_id = max_id + 1
            user = User(
                id=next_id, username=name, email=email, 
                password=password
            )

        # add it to the current database session
        db.session.add(user)
        db.session.commit()

        return user


def login(email, password):
    '''
    R2-1 and R2-2:
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    # make sure that the password and email meet the requirements
    if (password_helper(password) is True and email_helper(email) is True):
        valids = User.query.filter_by(email=email, password=password).all()
        if len(valids) != 1:
            return None
        return valids[0]


def title_desc(title_used, description):
    '''
    Check the title and description
      Parameters:
        title_used (string):    listing title
        description (string): listing description 
      Returns:
        True if title and description meet the requirements otherwise False
    '''
    # check if the title has been used:
    existed = Listing.query.filter_by(title=title_used).first()
    if (existed):
        print("This title already exists.")
        return False

    if len(title_used) <= 80:
        if (
            title_used[0] != " " and title_used[-1] != " " and 
            len(description) > 20 and len(description) < 2000 and 
            len(description) > len(title_used)
        ):
            title_regex = title_used.split(" ")
            for word in title_regex:
                if not re.match(r'^[a-zA-Z0-9]+$', word):
                    print("not alphanumeric")
                    return False
        else:
            print("spaces or description")
            return False
    else:
        print("title too long")
        return False
    return True
    

def check_price(price):
    '''
    Check the title and description
      Parameters:
        price:                listing price
      Returns:
        True if the price meets the requirements otherwise False
    '''
    if (10 <= price <= 10000):
        return True
    else:
        print("price lower than 10 or higher than 10000")
        return False


def check_date(date_modified):
    '''
    Check the title and description
      Parameters:
        date_modified:                listing date
      Returns:
        True if the date modified meets the requirements otherwise False
    '''
    if isinstance(date_modified, str):
        date_modified = datetime.strptime(date_modified, '%Y-%m-%d').date()
    lower = datetime(2021, 1, 2).date()
    upper = datetime(2025, 1, 2).date()
    if (lower <= date_modified <= upper):
        return True
    else:
        print("date is outside range")
    print("check date failed")


def check_owner(id):
    '''
    Check the title and description
      Parameters: 
        owner_id:             the owner's id of the listing 
      Returns:
        True if the email meets the requirements and the user is in 
        the db otherwise False
    '''
    # check the database to find the user's email
    user = User.query.filter_by(id=id).first()
    # the owner does exist in the db
    if user is None:
        print("user is none")
        return False
    if user.email == "":
        return False
    return True


def listing(
    listing_id, title, description, price, owner_id, 
    last_modified_date
):
    '''
    Create a new listing
      Parameters:
        id (int):                    listing id
        title (string):              listing title
        description (string):        listing description
        price (int):                 listing price
        owner_id (int):              listing owner id
        last_modified_date (string): last modified date of the listing
      Returns:
        True if listing creation succeeded otherwise False
    '''
    # check if the id has been used:
    existed = Listing.query.filter_by(id=listing_id).all()
    if len(existed) > 0:
        print("Sorry, this listing id is already created")
        return None
    if listing_id is not None:
        if (
            title_desc(title, description) is True and check_price(price) 
            is True and check_date(last_modified_date) is True and 
            check_owner(owner_id) is True
        ):
            # create a new user
            listing = Listing(
                id=listing_id, title=title, description=description, 
                price=price, owner_id=owner_id, 
                last_modified_date=last_modified_date
            )
            db.session.add(listing)
            db.session.commit()
            return listing
    else:
        if (
            title_desc(title, description) is True and 
            check_price(price) is True and 
            check_date(last_modified_date) is True and 
            check_owner(owner_id) is True
        ):
            max_id = db.session.query(func.max(Listing.id)).scalar()
            if max_id is None:
                max_id = 0
            next_id = max_id + 1
            listing = Listing(
                id=next_id, title=title, description=description, 
                price=price, owner_id=owner_id, 
                last_modified_date=last_modified_date
            )
            db.session.add(listing)
            db.session.commit()
            return listing
    return None


def update_listing(listing_id, title, description, price):
    '''
    R5-1, R5-2, R5-3, R5-4:
    Updates the title, description, and/or price of the listing, then 
    updates the date modified and makes the changes in the database
      Parameters:
        listing_id (int):     listing id number
        title (string):       listing title
        description (string): listing description
        price (int):          listing price
      Returns:
        False if any attribute is attempted to be updated with requirements
        that are not valid
    '''
    # use this to get the id of the listing in order to know what 
    # listing is being updated
    listing = Listing.query.filter_by(id=listing_id).first()
    if title is not None:
        # check the requirements of the title 
        title_regex = title.split(" ")
        for word in title_regex:
            if not re.match(r'^[a-zA-Z0-9]+$', word):
                print("not alphanumeric")
                return False
        if (len(title) <= 80 and title[0] != " " and title[-1] != " "):
            print("the title is valid")
            # check the date and that it is valid
            new_date_modified = datetime.now().date()
            date_valid = check_date(new_date_modified)
            if date_valid:
                # update the listing title
                listing.title = title
                print("update title")
                # update the last modified date of the listing 
                # to the current date
                listing.last_date_modified = new_date_modified
        else:
            print("title not valid")
            return False

    if description is not None:
        # check the requirements of the description
        if (
            len(description) > 20 and len(description) < 2000 and
            len(description) > len(listing.title)
        ):
            print("the desc is valid")
            # check the date and that it is valid
            new_date_modified = datetime.now().date()
            date_valid = check_date(new_date_modified)
            if date_valid:
                # update the listing description
                listing.description = description
                print("update desc")
                # update the last modified date of the listing 
                # to the current date
                listing.last_date_modified = new_date_modified
        else:
            print("desc not valid")
            return False

    if price is not None:
        # check the requirements of the price, and also make sure that 
        # the price is only increased when it is updated
        if 10 <= int(price) <= 10000 and int(price) > listing.price:
            print("price valid")
            # check the date and that it is valid
            new_date_modified = datetime.now().date()
            date_valid = check_date(new_date_modified)
            if date_valid:
                # update the listing price
                listing.price = price
                print("update price")
                # update the last modified date of the listing to 
                # the current date
                listing.last_date_modified = new_date_modified
        else:
            print("price not valid")
            return False

    # save the updated listing object
    db.session.commit()
    return True


def update_user(id, username, email, billing_address, postal_code):
    '''
    R3-1
    A user is only able to update his/her user name, user email,
    billing address, and postal code
      Parameters:
        name (string): user name
        email (string): user email
        billing_address (string): user billing_address
        postal_code (string): user postal_code
    '''

    # checking if user data in database equals current user data in current
    # session
    existed = User.query.filter_by(id=id).first()
    if existed is not None:
        # if yes, then update old user data in database
        user = User(
            id=id, username=username, email=email, 
            billing_address=billing_address, postal_code=postal_code
        )
        # updating old user data
        existed.username = username
        existed.email = email
        existed.billing_address = billing_address
        existed.postal_code = postal_code
        # saving updates to database
        db.session.commit()

        return existed
    return None


# R1-3
def email_helper(email):
    '''
    R1-1:
    Email cannot be empty. password cannot be empty.
    R1-3
    The email has to follow addr-spec defined in RFC 5322 (see 
    https://en.wikipedia.org/wiki/Email_address for a human-friendly 
    explanation). You can use external libraries/imports.
      Parameters:
        email (string): user email
    '''
    
    regex = re.compile(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9-]+\.[A-Z|a-z]{1,3}')
    # the email meets the requirements
    if (re.fullmatch(regex, email)): 
        return True
    else:
        return False
    

def password_helper(password):
    '''
    R1-1:
    Email cannot be empty. password cannot be empty.
    R1-4:
    Password has to meet the required complexity: minimum length 6, at least 
    one upper case, at least one lower case, 
    and at least one special character.
      Parameters:
        password (string): user password
    '''
    # lower case
    count_l = 0 
    # upper case
    count_u = 0 
    # special character
    count_s = 0 
        
    for ch in password:
        # uppercase characters
        if (ch.isupper()): 
            count_u += 1
        # lowecase characters
        if (ch.islower()): 
            count_l += 1
        # special character
        if ch in string.punctuation: 
            count_s += 1
        
    # check the validity of the password
    # password is not empty 
    if (password != ''): 
        # the password has 6 or more characters
        if (len(password) >= 6):  
            # more than one uppercase, lowercase and special characters
            if (count_u >= 1 and count_l >= 1 and count_s >= 1):  
                return True
            else:
                return False
        else:
            return False
    else:
        return False
     
    
def username_helper(username):
    '''
    R1-5:
        User name has to be non-empty, alphanumeric-only, and 
        space allowed only if it is not as the prefix or suffix.
    R1-6: 
        User name has to be longer than 2 characters and less than 20 
        characters.
    R3-1: 
        A user is only able to update his/her user name, user email, billing 
        address, and postal code.
    R3-4: 
        User name follows the requirements above.
        (postal code should be non-empty, alphanumeric-only, and no special 
        characters such as !)
    Parameters:
        username (string): user username
    '''
    # check for special characters
    last_ch = len(username) - 1
    # username is not empty
    if (username != " "): 
        if len(username) > 2 and len(username) < 20:
            if (username[0] != " " and username[last_ch] != " "):
                username_regex = username.split(" ")
                for ch in username_regex:
                    if not re.match(r'^[a-zA-Z0-9]*$', ch):
                        return False
                    else:
                        return True
            else: 
                return False
        else:
            return False
    else:
        return False


def postal_code_helper(postal_code):
    '''
    R3-2
    postal code should be non-empty, alphanumeric-only, and no special 
    characters such as !
    R3-3
    Postal code has to be a valid Canadian postal code
      Parameters:
        postal_code (string): user postal_code
    '''
    # special character
    count_s = 0
    # digits
    num_count = 0
    # alphabets
    char_count = 0
    
    for ch in range(len(postal_code)):
        # count the number of special characters
        if postal_code in string.punctuation:
            count_s += 1

        # checking if empty string
        if (postal_code[ch] != ""):
            # checking if letter
            if (ch == 0 or ch == 2 or ch == 4) and postal_code[ch].isalpha():
                char_count += 1
            # checking if number
            if (ch == 1 or ch == 3 or ch == 5) and postal_code[ch].isdigit():
                num_count += 1
    # checking if any special characters
    if (count_s == 0):
        # if 3 letters and 3 numbers
        if (num_count == 3 and char_count == 3):
            return True
        else:
            return False
