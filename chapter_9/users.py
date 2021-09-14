class User():
    """A simple attempt to model a user."""
    
    def __init__(self, first_name, last_name, age, gender):
        """Initialize first name, last name, age, and gender attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender
        
    def describe_user(self):
        """Prints a summary of the users information."""
        print(self.first_name.title() + " " + self.last_name.title() +
              " is a " + str(self.age) + " year old who identifies as " +
              self.gender + ".")
        
    
    def greet_user(self):
        """Prints a personlized greeting to the user."""
        print("Welcome, " + self.first_name.title() + "!")
        
my_user = User('logyn', 'powers', 33, 'female')
my_user.describe_user()
my_user.greet_user()        

bran_user = User('brandon', 'powers', 32, 'male')
bran_user.describe_user()
bran_user.greet_user()

mom_user = User('vicki', 'brown', 61, 'female')
mom_user.describe_user()
mom_user.greet_user()