from xxlimited import new
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

    # setting default values for user variables
    id = 1
    billing_address = ""
    postal_code = ""
    account_bal = 100

    # create a new user
    user = User(id=id, username=name, email=email, password=password, billing_address=billing_address, postal_code=postal_code, account_bal=account_bal)
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
    new_name = name
    new_email = email
    new_billing_address = billing_address
    new_postal_code = postal_code

    # accessing user data
    q = db.session.query(User)
    # check if user id is correct
    q = q.filter(User.id==1)
    # updating old user data
    record = q()
    record.name = new_name
    record.email = new_email
    record.billing_address = new_billing_address
    record.postal_code = new_postal_code
    # saving updates to database
    db.session.commit()

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