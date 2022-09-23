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
    def set_ratings(self, rating):
        self.rating = rating

    # getter method for comments
    def get_comments(self):
        return self.comment

    # setter method for comments
    def set_comments(self, comment):
        self.comment = comment