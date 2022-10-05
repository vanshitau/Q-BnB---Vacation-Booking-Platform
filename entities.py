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