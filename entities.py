# reviews entity
class Reviews:
    # initializing components of reviews entity
    def __init__(self, name = "", rating = 0, comment = ""):
         self.rating = rating
         self.comment = comment
         self.name = name

    # getter method for name
    def get_name(self):
        return self.name

    # setter method for name
    def set_name(self, name):
        self.name = name
      
    # getter method for ratings
    def get_ratings(self):
        return self.rating
      
    # setter method for ratings
    def set_ratings(self, rating):
        self.rating = rating

    # getter method for comments
    def get_comments(self):
        return self.comment

    # setter method for comments
    def set_comments(self, x):
        self.comment = x

#listings entity
class Listing:
    def __init__(self, price = 0, rating = 0, location="", size = 0, description = ""): 
         self._price = price
         self._rating = rating
         self._location = location
         self._size = size
         self._description = description
      
    # getter methods

    #getter method for the price
    def get_price(self):
        return self._price
    
    #getter method for the rating
    def get_rating(self):
        return self._rating

    #getter method for the location
    def get_location(self):
        return self._location

    #getter method for the size
    def get_size(self):
        return self._size
        
    #getter method for the description
    def get_description(self):
        return self._description
      
    #setter methods

    #setter method for the price
    def set_price(self,price):
        self._price = price

    #setter method for the rating   
    def set_rating(self,rating):
        self._rating = rating

    #setter method for the location     
    def set_location(self,location):
        self._location = location

    #setter method for the size     
    def set_size(self,size):
        self._size = size

    #setter method for the description      
    def set_description(self,description):
        self._description = description
        
# bookings entity
class Bookings:
    # initializing components of reviews entity
    def __init__(self, verification = "", date = "", duration = ""):
         self.verification = verification
         self.date = date
         self.duration = duration
         self.is_paid = is_paid
      
    # getter method for verification
    def get_verfication(self):
        return self.verification
      
    # setter method for verification
    def set_verification(self, verify):
        self.verification = verify

    # getter method for date
    def get_date(self):
        return self.date

    # setter method for date
    def set_date(self, date):
        self.date = date

     # getter method for duration
    def get_duration(self):
        return self.duration

    # setter method for duration
    def set_duration(self, duration):
        self.duration = duration

    # getter method for paid
    def get_is_paid(self):
        return self.is_paid

    # setter method for paid
    def set_is_paid(self, paid):
        self.is_paid = paid

# user entity
class User:
    # initializing components of user entity
    def __init__(self, id = 0, username = "", email = "", password = "", account_bal = 0):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.account_bal = account_bal

    # getter method for user id
    def get_id(self):
        return self.id
      
    # setter method for user id
    def set_id(self, myId):
        self.id = myId

    # getter method for username
    def get_username(self):
        return self.username
    
    # setter method for username
    def set_username(self, username):
        self.username = username

    # getter method for email
    def get_email(self):
        return self.email

    # setter method for email
    def set_email(self, email):
        self.email = email

    # getter method for password
    def get_password(self):
        return self.password

    # setter method for password
    def set_password(self, password):
        self.password = password

    # getter method for account balance
    def get_account_balance(self):
        return self.account_bal

    # setter method for account balance
    def set_account_balance(self, balance):
        self.account_bal = balance
