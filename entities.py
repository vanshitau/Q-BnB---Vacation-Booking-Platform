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
    
    #getter method for the rating
    def get_title(self):
        return self._title

    #getter method for the location
    def get_id(self):
        return self._id

    #getter method for the size
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

    #setter method for the description      
    def set_title(self,title):
        self._title = title

    #setter method for the listing id     
    def set_id(self,id):
        self._id = id

    #setter method for the owner id      
    def set_owner_id(self,owner_id):
        self._owner_id = owner_id

    #setter method for the last modified date       
    def set_last_modified_date(self,last_mod_date):
        self._last_modified_date = last_mod_date


    