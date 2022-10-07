from qbay import app
from flask_sqlalchemy import SQLAlchemy


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

#need an email function
#R1-2- A user is uniquely identified by his/her user id

#R1-4
def password_helper(password):
        count_l = 0 #lower case
        count_u = 0 #upper case
        count_s = 0 #special character
        for ch in range(len(password)):
            if (ch.isUpper): #uppercase characters
                count_u+=1
            elif (ch.isLower): #lowecase characters
                count_l+=1
            elif (ch.punctuation): #special character
                count_s+=1
        
        #check the validity of the password
        if (password != ""): #password is not empty
            if (len(password) >= 6):  #the password has 6 or more characters
                if count_u > 0:  #more than one uppercase character
                    if count_l >0: #more than one lowercase character
                        if count_s>0: #more than one special character
                            return password

#R1-5 and 
def username_helper(username):
        last_ch = username(len)-1
        if (username != ""): #username is not empty
            if(username.isalnum()): #username is alphanumeric
                if(username[0] != " " and username[last_ch] != " "): #the first and last characters are not a space
                    if(len(username) > 2 and len(username) < 20):
                        return username

#R3-1: 
#R3-2
def postal_code_helper(postal_code):
        count_s = 0
        num_count = 0
        char_count = 0

        for ch in range(len(postal_code)):
            if (postal_code[ch].punctuation):
                count_s+=1

            # checking if number
            if ch % 2 == 0:
                num_count += 1
            # checking if letter
            else:
                char_count += 1

        if(postal_code != ""):
            if (postal_code.isalnum()):
                if(count_s == 0):
                    if (num_count == 3 and char_count == 3):
                        return postal_code