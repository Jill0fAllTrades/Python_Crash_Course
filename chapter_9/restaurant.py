class Restaurant():
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initializes restaurant name and cuisine attributes"""
        self.name = restaurant_name.title()
        self.cuisine = cuisine_type
        self.set_number_served = 10
        
    def increment_number_served(self, increment):
        """Adds the increment to the number of people served today."""
        self.set_number_served += increment
        
    def read_people_served(self, number_of_people):
        """Prints how many people have been served at this restaurant today"""
        print(self.name + ' has served ' + str(self.set_number_served) +
              ' people today.')
    
    def describe_restaurant(self):
        """Describes the restaurant."""
        print(self.name.title() + " serves " + self.cuisine + " food.")
    
    
    def open_restaurant(self):
        """Simulates opening the restaurant."""
        print(self.name.title() + " is now open and ready to serve you!")
        
restaurant = Restaurant('chipotle', 'tex-mex')

print(restaurant.name)
print(restaurant.cuisine)
restaurant.describe_restaurant()
restaurant.open_restaurant()
restaurant.increment_number_served(11)
restaurant.read_people_served(1) 