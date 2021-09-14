def sandwich_toppings(*toppings):
    """takes topping input and prints a summary of sandwich being ordered."""
    print("\nYour sandwich will have the following on it:")
    for topping in toppings:
        print("-" + topping)