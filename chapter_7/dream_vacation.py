destinations_dict = {}

polling_active = True

while polling_active:
    name = input("What is your name?\n")
    response = input("If you could visit one place in the world, where" +
                    " would you go?\n")
    
    destinations_dict[name] = response
    
    answer = input("would someone else like to take this poll?\n\t" +
                   "Type yes or no.\n")
    if answer == 'no':
        polling_active = False
        print("\nThanks for taking this poll!\n")

print("Here are the poll results. The most desired destinations are:")
      
for name, response in destinations_dict.items():
    print("-" + response.title())
#bug: only lists last response        
