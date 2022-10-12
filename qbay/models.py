from curses.ascii import isalnum, isalpha
from xxlimited import new
from qbay import app
from flask_sqlalchemy import SQLAlchemy
import string

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
        Balance should be initialized as 100 at the time of registration. (free $100 dollar signup bonus).
    '''
    id = db.Column(db.Integer, nullable=False)
    # added default value for billing_address = ""
    billing_address = db.Column(db.String(150), default="",  nullable=False)
    # added default value of account_bal = 100
    account_bal = db.Column(db.Integer, default=100, nullable=False)
    # added default value of postal_code = ""
    postal_code = db.Column(db.String(20), default="", nullable=False)
    username = db.Column(
        db.String(80), nullable=False)
    email = db.Column(
        db.String(120), unique=True, nullable=False, 
        primary_key=True)
    password = db.Column(
        db.String(120), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


# create all tables
db.create_all()


def register(name, email, password):
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
        return False

    # create a new user
    user = User(username=name, email=email, password=password)
    # add it to the current database session
    db.session.add(user)
    db.session.commit()

    return True


def login(email, password):
    '''
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    valids = User.query.filter_by(email=email, password=password).all()
    if len(valids) != 1:
        return None
    return valids[0]


def update(name, email, billing_address, postal_code):
    '''
    R3-1
    A user is only able to update his/her user name, user email, billing address, and postal code
      Parameters:
        name (string): user name
        email (string): user email
        billing_address (string): user billing_address
        postal_code (string): user postal_code
    '''
    # checking if user data in database equals current user data in current session
    user = User.query.filter_by(User.username==name).all()
    if (user):
        # if yes, then update old user data in database
        update_helper(name, email, billing_address, postal_code)
    return False
    

def update_helper(name, email, billing_address, postal_code):
    '''
    R3-1
    helper function to update his/her user name, user email, billing address, and postal code
      Parameters:
        name (string): user name
        email (string): user email
        billing_address (string): user billing_address
        postal_code (string): user postal_code
    '''
    # accessing user data
    q = db.session.query(User)
    # check if user id is correct
    q = q.filter(User.id==1) # needed id generator
    # updating old user data
    record = q()
    record.name = name
    record.email = email
    record.billing_address = billing_address
    record.postal_code = postal_code
    # saving updates to database
    db.session.commit()

    return True


def username_helper(username):
    '''
    R1-5:
        User name has to be non-empty, alphanumeric-only, and space allowed 
        only if it is not as the prefix or suffix.
    R1-6: 
        User name has to be longer than 2 characters and less than 20 characters.
    R3-1: 
        A user is only able to update his/her user name, user email, billing address, and postal code.
    R3-4: 
        User name follows the requirements above.
        (postal code should be non-empty, alphanumeric-only, and no special characters such as !)
    Parameters:
        username (string): user username
    '''
    #check for special characters
    count_s = 0
    for ch in username:
        if ch in string.punctuation:
            count_s += 1

    last_ch = len(username) - 1
    # checking if username is not empty
    if (username != ""):
        # checking if length of username is within requirements
        if len(username) > 2 and len(username) < 20:
            for ch in range(len(username)):
                # checking if the first character and last character is a space 
                if (username[0] != "" and username[last_ch] != "" and count_s == 0):
                    # checking if the username is alphanumeric
                    if (username[ch].isalnum()): 
                        return True
                    else:
                        return False
                else:
                    return False
        else:
            return False
    else:
        return False


def postal_code_helper(postal_code):
    '''
    R3-2
    postal code should be non-empty, alphanumeric-only, and no special characters such as !
    R3-3
    Postal code has to be a valid Canadian postal code
      Parameters:
        postal_code (string): user postal_code
    '''
    # initializing counters
    count_s = 0
    num_count = 0
    char_count = 0
    
    for ch in range(len(postal_code)):
        # checking if any punctuation
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
    # if no punctuation
    if (count_s == 0):
        # if 3 letters and 3 numbers
        if (num_count == 3 and char_count == 3):
            return True
        else:
            return False