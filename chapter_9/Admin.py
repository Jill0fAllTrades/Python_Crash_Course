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
        
        
class Admin(User):
    """A simple attempt at representing an admin subclass of User."""
    
    def __init__(self, first_name, last_name, age, gender):
        """
        Initializes attributes from the parent class.
        Then initializes attributes specific to this subclass.
        """
        super().__init__(first_name, last_name, age, gender)
        self.priveleges = "can add post", "can delete post", "can ban user"
        
    
            
class Priveleges():
    """Represents a class that defines priveleges that a User has."""
    
    def show_priveleges(self):
        """Prints the priveleges granted to this type of User(Admin)."""
        print("This user:")
        for privelege in self.priveleges:
            print(privelege)
##Left off on assignment 9-8, store a list of strings in Priveleges class
brandon = User('brandon', 'powers', 32, 'male')
brandon.describe_user()
logyn = Admin('logyn', 'powers', 33, 'female')
logyn.describe_user()
logyn.show_priveleges()

