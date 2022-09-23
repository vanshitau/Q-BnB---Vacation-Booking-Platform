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
# bookings entity
class Bookings:
    # initializing components of reviews entity
    def __init__(self, verification = "", date = 0, duration = ""):
         self.verification = verification
         self.date = date
         self.duration = duration
      
    # getter method for verification
    def get_verfication(self):
        return self.verification
      
    # setter method for verification
    def set_verification(self, x):
        self.verification = x

    # getter method for date
    def get_date(self):
        return self.date

    # setter method for date
    def set_date(self, x):
        self.date = x

     # getter method for duration
    def get_duration(self):
        return self.duration

    # setter method for date
    def set_duration(self, x):
        self.duration = x