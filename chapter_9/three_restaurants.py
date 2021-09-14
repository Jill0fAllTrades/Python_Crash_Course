class Restaurant():
    """A simple attempt to model a restaurant."""
    
    def __init__(self, restaurant_name, cuisine_type):
        """Initializes name and cuisine attributes"""
        self.name = restaurant_name
        self.cuisine = cuisine_type
    
    def describe_restaurant(self):
        """Describes the restaurant."""
        print(self.name.title() + " serves " + self.cuisine + " food.")
    
    
    def open_restaurant(self):
        """Simulates opening the restaurant."""
        print(self.name.title() + " is now open and ready to serve you!")
        
my_restaurant = Restaurant('chipotle', 'tex-mex')
brans_restaurant = Restaurant('choongman', 'korean')
moms_restaurant = Restaurant('world of good', 'global')

moms_restaurant.describe_restaurant()
brans_restaurant.describe_restaurant()
my_restaurant.describe_restaurant()