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


#R1-2- A user is uniquely identified by his/her user id
#R1-3
def email_helper(email):
    count_a = 0
    for ch in range(len(email)):
        if email[ch] == "@":
            count_a +=1
    
    
    if count_a == 1:
        #find the index of @
        index_a = email.index("@")

    #before_a = [left]
    before_a = email[0:index_a]

    #after_a = [right]
    after_a= email[index_a:]
    
    count_d = 0
    #len of left and len of right--> see if it meets the requirements
    if len(before_a) == 64 and len(after_a) == 255:
        #check if after_a has a dot
        for a in range(len(after_a)):
            if(after_a[a] == "." and after_a[a-1] != "."):
                count_d +=1

        if count_d == 0:
            for b in before_a:
                if(a.isalpha() or a.isdigit or (a == "-" or "." or "_")):
                    return email


    #if right side has a dot and it is not the last ch
    #letters, digits, -, . , _
   
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
                            self.password = password
    
#R1-5 and 
def username_helper(self, username):
        last_ch = username(len)-1
        if (username != ""): #username is not empty
            if(username.isalnum()): #username is alphanumeric
                if(username[0] != " " and username[last_ch] != " "): #the first and last characters are not a space
                    self.username = username

#R3-1: 


#R3-2
def postal_code_helper(self, postal_code):
        count_s = 0
        for ch in postal_code:
            if (ch.punctuation):
                count_s+=1

        if(postal_code != ""):
            if (postal_code.isalnum()):
                if(count_s == 0):
                    self.postal_code = postal_code