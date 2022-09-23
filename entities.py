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