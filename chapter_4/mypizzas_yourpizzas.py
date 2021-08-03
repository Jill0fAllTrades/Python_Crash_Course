#think of 3 kinds of pizza: pepporoni cheese mushroom

#store names in a list
pizzas = ['pepperoni', 'cheese', 'mushroom']
#print the name of each type of pizza with a loop
for pizza in pizzas:
    print("Should we have " + pizza + " pizza?")
    
print("I don't know what type of pizza I want!!")

#TODO make a copy and call it friend_pizzas
bran_pizzas = pizzas[:]
#TODOadd a new pizza to original list
pizzas.append('hawaiian')
#TODOadd a different pizza to friend_pizzas
bran_pizzas.append('BBQ chicken')
#TODO print "my fave pizzas are" and original list
print("My favorite pizzas are:" + str(pizzas))
#TODO print my friends fave pizzas are and friends list
print("Brandon's fave pizzas are:" + str(bran_pizzas))