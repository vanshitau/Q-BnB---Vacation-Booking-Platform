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


    