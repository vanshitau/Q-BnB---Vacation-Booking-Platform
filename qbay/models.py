from sqlalchemy import PrimaryKeyConstraint
from qbay import app
from flask_sqlalchemy import SQLAlchemy
#from entities import *


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
    owner_id = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username

class Listing(db.Model):
    id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(80), nullable=False, primary_key=True)
    description = db.Column(db.String(500), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    last_modified_date = db.Column(db.String(80), nullable=False)
    owner_id = db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        return '<User %r>' % self.title




# create all tables
db.create_all()


def register(owner_id, name, email, password):
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
    user = User(owner_id=owner_id,username=name, email=email, password=password)
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

def title_desc(id,title,description,last_modified_date, price,owner_id):
    '''
    Check the title and description
      Parameters:
        id (string):     listing id
        title (string):    listing title
        description (string): user password
        last_modified_date:   listing last modified date
        price:                listing price
        owner_id:             owner id of the listing
      Returns:
        True if title and description meet the requirements otherwise False
    '''
    #fix - check to see if all characters are alphanum
    #this does not check to see if all the characters are alphanumeric - to do this you would need to use regex
    # and check to see if each character is a-z A-z or 0-9

    #check to see if the title exists
    existed = Listing.query.filter_by(title=title).first()

    #if the title is not an empty sting, check to see if the first and last char are not spaces
    #make sure the length of the description is more than the title length and is <2000 and >20
    if not(existed):
        if (len(title) > 0):
            if (title[0] != " ") and title[:1].isalnum() and (len(title) <= 80) and  title[-1] != " " and len(description) > 20 and len(description)< 2000 and (len(description) > len(title)) :
                return True

    # create a new user
    listing = Listing(id=id, title=title, description=description,last_modified_date=last_modified_date, price=price,owner_id=owner_id)
    # add it to the current database session
    db.session.add(listing)
    # actually save the user object
    db.session.commit()

    return False
    
def check_price(price):
    '''
    Check the title and description
      Parameters:
        price:                listing price
      Returns:
        True if the price meets the requirements otherwise False
    '''
    if(10<=price<=10000):
        return price

def check_date(date_modified):
    '''
    Check the title and description
      Parameters:
        date_modified:                listing date
      Returns:
        True if the date modified meets the requirements otherwise False
    '''
    if ('2021-01-02' <= date_modified <= '2025-01-02'):
        return date_modified

def check_owner(email, owner_id):
    '''
    Check the title and description
      Parameters:
        email:                the owner's email of the listing 
        owneer_id:            the owner's id of the listing 
      Returns:
        True if the email  meets the requirements and the user is in the db otherwise False
    '''
    
    #check the database to find the user's email
    user = User.query.filter_by(email=owner_id).first()
   # listing_email = user.email
    #the owner does exist in the db
    if user:
        #the email is not empty
        if email != '':
            return True
    else:
        return False








    





    


