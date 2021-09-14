def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print("\nYour " + str(size) +
          " inch pizza will have the following toppings:")
    for topping in toppings:
        print("-" + topping)
    
