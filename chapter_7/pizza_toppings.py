#write a loop prompting user to input a series of pizza toppings till
#they enter quit
    

#as they enter each topping, print a message saying you'll add that topping
    #to their pizza
prompt = "Tell me what topping you would like on your pizza:\n"
prompt += "(Enter 'quit' to finish.)\n"

toppings = ""
while toppings != 'quit': #while toppings are not equal to 'quit'
    toppings = input(prompt) #type the question and prompt and
    print("Adding " + toppings + " to your pizza!\n") 
    if toppings == 'quit':
        print("Got it.")