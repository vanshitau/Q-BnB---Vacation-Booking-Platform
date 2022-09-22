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
    def __init__(self, price=0, rating=0, location="", size=0, description=""): 
         self._price=price
         self._rating = rating
         self._location = location
         self._size=size
         self._description = description
      
    # getter method
    def get_price(self):
        return self._price

    def get_rating(self):
        return self._rating

    def get_location(self):
        return self._location

    def get_size(self):
        return self._size
        
    def get_description(self):
        return self._description
      
    #setters
    def set_price(self,price):
        self._price = price
            
    def set_rating(self,rating):
        self._rating = rating
            
    def set_location(self,location):
        self._location = location
            
    def set_size(self,size):
        self._size = size
            
    def set_description(self,description):
        self._description = description


    