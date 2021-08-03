#think of 3 kinds of pizza: pepporoni cheese mushroom

pizzas = ['pepperoni', 'cheese', 'mushroom']
for pizza in pizzas:
    print("Should we have " + pizza + " pizza?")
    
print("I don't know what type of pizza I want!!")

bran_pizzas = pizzas[:]
pizzas.append('hawaiian')
bran_pizzas.append('BBQ chicken')

print("My favorite pizzas are:")
for pizza in pizzas:
    print("-" + pizza)
    
print("...and Brandon's fave pizzas are:")
for pizza in bran_pizzas:
    print("-" + pizza)