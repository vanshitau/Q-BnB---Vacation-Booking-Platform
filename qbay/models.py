from qbay import app
from flask_sqlalchemy import SQLAlchemy

import string
import re
import random


'''
This file defines data models and related business logics
'''


db = SQLAlchemy(app)


class User(db.Model):
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
    Register a new user
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
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
    # actually save the user object
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


#R1-2- A user is uniquely identified by his/her user id
def user_id_helper(user):
    #generate a random id for the user
    for i in range(len(user)):
        id = random.randint(1,1000)
    
    #check if the user id already exists
    existed = id.query.filter_by(user=user).first()


#R1-3
def email_helper(email):
    '''
    R1-1:
    Email cannot be empty. password cannot be empty.
    R1-3
    The email has to follow addr-spec defined in RFC 5322 (see https://en.wikipedia.org/wiki/Email_address for 
    a human-friendly explanation). You can use external libraries/imports.
      Parameters:
        email (string): user email
    '''
    regex = re.compile("^[a-zA-Z0-9-._]+@[a-zA-Z0-9]+\.[a-z]{1,3}$")
    #the email meets the requirements
    if (re.match(regex, email)): 
        return True
    else:
        return False
    
    
#R1-4
def password_helper(password):
    '''
    R1-1:
    Email cannot be empty. password cannot be empty.
    R1-4:
    Password has to meet the required complexity: minimum length 6, at least one upper case, at least one lower case, 
    and at least one special character.
      Parameters:
        password (string): user password
    '''
    #lower case
    count_l = 0 
    #upper case
    count_u = 0 
    #special character
    count_s = 0 
        
    for ch in password:
        #uppercase characters
        if (ch.isupper()): 
            count_u+=1
        #lowecase characters
        if (ch.islower()): 
            count_l+=1
        #special character
        if ch in string.punctuation: 
            count_s+=1
        
    #check the validity of the password
    #password is not empty
    if (password != ""): 
        #the password has 6 or more characters
        if (len(password) >= 6):  
            #more than one uppercase, lowercase and special characters
            if (count_u >=1 and count_l >=1 and count_s >= 1):  
                return True
            else:
                return False
        else:
            return False
    else:
        return False
     
    
#R1-5 and 
def username_helper(username):
    '''
    R1-5:
    User name has to be non-empty, alphanumeric-only, and space allowed only if it is not as the prefix or suffix.
    Parameters:
        username (string): user username
    '''
    #check for special characters
    last_ch = len(username)-1
    #username is not empty
    if (username != ""): 
        for ch in range(len(username)):
            #the first character and last character cannot be a space 
            if (username[0] != "" and username[last_ch] != ""): 
                #the username is alphanumeric
                if (username[ch].isalnum()): 
                    return True
                else:
                    return False
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
    #special character
    count_s = 0
    #digits
    num_count = 0
    #alphabets
    char_count = 0
    
    for ch in range(len(postal_code)):
        #count the number of special characters
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
        #check if it is a valid canadian postal code
        if (num_count == 3 and char_count == 3): 
            return True
        else:
            return False