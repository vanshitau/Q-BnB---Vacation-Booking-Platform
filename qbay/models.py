from qbay import app
from flask_sqlalchemy import SQLAlchemy
# import library to work with the current date
import datetime as dt
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

class Listing(db.Model):
    '''
    Initiates the listing class and all of the columns of the listing
    '''
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    title = db.Column(db.String(80), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    last_modified_date = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


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
    R2-1 and R2-2:
    Check login information
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    '''
    # make sure that the password and email meet the requirements
    if (password_helper(password) == True and email_helper(email) == True):
        valids = User.query.filter_by(email=email, password=password).all()
        if len(valids) != 1:
            return None
        return valids[0]

def listing(id, title, description, price, owner_id, last_modified_date):
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
    existed = Listing.query.filter_by(id=id).all()
    if existed:
        return False

    # create a new listing
    listing = Listing(id=id, title=title, description=description, 
        price=price, owner_id=owner_id, last_modified_date=last_modified_date)
    # add it to the current database session
    db.session.add(listing)
    # actually save the listing object
    db.session.commit()
    return True

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
    listing = Listing.query.get(listing_id)

    # if the the title is not being updated, pass
    if title == None:
        pass
    else:
        # check the requirements of the title 
        if (title[:1].isalnum()) and (len(title) <= 80):
            # update the listing title
            listing.title = title  
            # update the last modified date of the listing to the current date
            Listing.date_modified = dt.date.today()      
        else:
            return False

    # if the the description is not being updated, pass
    if description == None:
        pass
    else:
        # check the requirements of the description
        if (len(description) > 20 and len(description) < 2000 and
            len(description) > len(title)):
            # update the description of the listing
            listing.description = description
            # update the last modified date of the listing to the current date
            Listing.date_modified = dt.date.today()
        else:
            return False

    # if the the price is not being updated, pass
    if price == None:
        pass
    else:
        # check the requirements of the price, and also make sure that 
        # the price is only increased when it is updated
        if 10 <= price <= 10000 and price > listing.price:
            # update the price of the listing
            listing.price = price
            # update the last modified date of the listing to the current date
            Listing.date_modified = dt.date.today()
        else:
            return False

    # save the updated listing object
    db.session.commit()


def email_helper(email):
    '''
    code copied from vashita that was used in order to prevent reused code
    '''
    regex = re.compile("^[a-zA-Z0-9-._]+@[a-zA-Z0-9]+\.[a-z]{1,3}$")
    if (re.match(regex, email)):
        return True
    else:
        return False


def password_helper(password):
    '''
    code copied from vashita that was used in order to prevent reused code
    '''
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