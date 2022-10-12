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
    #listing (id, title, description, price, last_modified_date, owner_id)
    def __init__(self, id = 0, title = "", description = "", price = 0, last_modified_date = "", owner_id = 0): 
         self._price = price
         self._title = title
         self._id = id
         self._description = description
         self._last_modified_date = last_modified_date
         self._owner_id = owner_id

      
    # getter methods

    #getter method for the price
    def get_price(self):
        return self._price
    
    #getter method for the title
    def get_title(self):
        return self._title

    #getter method for the id
    def get_id(self):
        return self._id

    #getter method for the last modified date
    def get_modified_date(self):
        return self._last_modified_date
        
    #getter method for the description
    def get_description(self):
        return self._description
    
    #getter method for the owner's id
    def get_owner_id(self):
        return self._owner_id
      
    #setter methods

    #setter method for the price
    def set_price(self,price):
        self._price = price

    #setter method for the description      
    def set_description(self,description):
        self._description = description

     #setter method for the id      
    def set_id(self,id):
        self._id = id
    
    #setter method for the owner id      
    def set_owner_id(self,owner_id):
        self._owner_id = owner_id
    
    #setter method for the title      
    def set_title(self,title):
        self._title = title

    #setter method for the last modified date     
    def set_modified_date(self,mod_date):
        self._last_modified_date = mod_date



        
# bookings entity
class Bookings:
    # initializing components of reviews entity
    def __init__(self, verification = "", date = "", duration = "", is_paid = ""):
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
    def __init__(self, id = 0, username = "", email = "", password = "", account_bal = 0, billing_address = "", postal = ""):
        self.id = id
        self.username = username
        self.email = email
        self.password = password
        self.account_bal = account_bal
        self.billing_address = billing_address
        self.postal = postal

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

    # getter method for billing address
    def get_address(self):
        return self.billing_address
      
    # setter method for billing address
    def set_billing_address(self, billing_address):
        self.id = billing_address

    # getter method for postal code
    def get_postal(self):
        return self.postal
      
    # setter method for postal code
    def set_postal(self, postal):
        self.postal = postal