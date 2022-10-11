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
    id = db.Column(db.Integer, nullable=False)
    billing_address = db.Column(db.String(150), nullable=False)
    account_bal = db.Column(db.Integer, nullable=False)
    postal_code = db.Column(db.String(20), nullable=False)
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


def register(id, name, email, password, billing_address, postal_code, account_bal):
    '''
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

    account_bal = 100
    postal_code = ""
    billing_address = ""

    # create a new user
    user = User(id=id, username=name, email=email, password=password, billing_address=billing_address, postal_code=postal_code, account_bal=account_bal)

    # add it to the current database session
    db.session.add(user)
    db.session.commit()

    if User.query.filter_by(id=id):
        new_account_bal = User.query.filter_by(account_bal=account_bal).all()
        if new_account_bal == 100:
            return True
        
        new_postal_code = User.query.filter_by(postal_code=postal_code).all()
        if new_postal_code == '':
            return True
        
        new_billing_address = User.query.filter_by(billing_address=billing_address).all()
        if new_billing_address == '':
            return True
        else: 
            return False

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
    if (db.filter_by(User.username==name, User.email==email, User.billing_address==billing_address, User.postal_code==postal_code).all()):
        # if yes, then update old user data in database
        update_helper(name, email, billing_address, postal_code)
    

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
    q = q.filter(User.id==1)
    # updating old user data
    record = q()
    record.name = name
    record.email = email
    record.billing_address = billing_address
    record.postal_code = postal_code
    # saving updates to database
    db.session.commit()

    return True


#R1-5
def username_helper(username):
    last_ch = len(username)-1
    if (username != ""): #username is not empty
        if(username.isalnum()): #username is alphanumeric
            if(username[0] != " " and username[last_ch] != " "): #the first and last characters are not a space
                if(len(username) > 2 and len(username) < 20):
                    return True
                else:
                    False

def password_helper(password):
        count_l = 0 #lower case
        count_u = 0 #upper caseS
        count_s = 0 #special character
        #if (len(password) >=6):
        for ch in password:
            if (ch.isupper()): #uppercase characters
                count_u+=1
            if (ch.islower()): #lowecase characters
                count_l+=1
            if ch in string.punctuation: #special character
                count_s+=1
        
        #check the validity of the password
        if (password != ""): #password is not empty
            if (len(password) >= 6):  #the password has 6 or more characters
                if (count_u >=1 and count_l >=1 and count_s >= 1):  #more than one uppercase character
                    return True
                else:
                    return False
            else:
                return False

#R3-1: 
#R3-2
def postal_code_helper(postal_code):
    '''
    R3-2
    postal code should be non-empty, alphanumeric-only, and no special characters such as !
    R3-3
    Postal code has to be a valid Canadian postal code
      Parameters:
        postal_code (string): user postal_code
    '''
    count_s = 0
    num_count = 0
    char_count = 0
    
    for ch in range(len(postal_code)):
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
    if (count_s == 0):
        if (num_count == 3 and char_count == 3):
            return True
        else:
            return False