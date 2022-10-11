from qbay import app
from flask_sqlalchemy import SQLAlchemy

import string
import re


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
#R1-3
def email_helper(email):
    regex = re.compile("^[a-zA-Z0-9-_]+@[a-zA-Z0-9]+\.[a-z]{1,3}$")
    if (re.match(regex, email)):
        return True
    else:
        return False
    # count_a = 0
    # for ch in range(len(email)):
    #     if email[ch] == "@":
    #         count_a +=1
    
    
    # if count_a == 1:
    #     #find the index of @
    #     index_a = email.index("@")

    # #before_a = [left]
    # before_a = email[0:index_a]

    # #after_a = [right]
    # after_a= email[index_a:]
    
    # count_d = 0
    # #len of left and len of right--> see if it meets the requirements
    # if len(before_a) == 64 and len(after_a) == 255:
    #     #check if after_a has a dot
    #     for a in range(len(after_a)):
    #         if(after_a[a] == "." and after_a[a-1] != "."):
    #             count_d +=1

    #     if count_d == 0:
    #         for b in before_a:
    #             if(a.isalpha() or a.isdigit() or (a == "-" or "." or "_")):
    #                 return email


    #if right side has a dot and it is not the last ch
    #letters, digits, -, . , _
   
#R1-4
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
     
    
#R1-5 and 
def username_helper(username):
        last_ch = len(username)-1
        if (username != ""): #username is not empty
            if(username.isalnum()): #username is alphanumeric
                if(username[0] != " " and username[last_ch] != " " and username[1:last_ch] == ""): #the first and last characters are not a space
                    return True
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