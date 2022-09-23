# reviews entity
class Reviews:
    # initializing components of reviews entity
    def __init__(self, rating = 0, comment = ""):
         self.rating = rating
         self.comment = comment
      
    # getter method for ratings
    def get_ratings(self):
        return self.rating
      
    # setter method for ratings
    def set_ratings(self, x):
        self.rating = x

    # getter method for comments
    def get_comments(self):
        return self.comment

    # setter method for comments
    def set_comments(self, x):
        self.comment = x

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
    def set_username(self, x):
        self.username = x

    # getter method for email
    def get_email(self):
        return self.email

    # setter method for email
    def set_email(self, x):
        self.email = x

    # getter method for password
    def get_password(self):
        return self.password

    # setter method for password
    def set_password(self, x):
        self.password = x

    # getter method for account balance
    def get_account_balance(self):
        return self.account_bal

    # setter method for account balance
    def set_account_balance(self, x):
        self.account_bal = x