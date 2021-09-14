#make a list and fill it with names of sandwiches
sammies = ['reuben', 'monte cristo', 'BLT', 'lox bagel', 'grilled cheese']

#empy list called finished sandwiches
finished_sammies = []

#loop through sandwich order,print i made your blah sandwich
while sammies:
    current_sammy = sammies.pop()
    print("I made your " + current_sammy + ".")
    
    finished_sammies.append(current_sammy)

print("\n")
#At end, list each sandwich that was made

print("The following sandwiches were made:\n")
for sandwich in finished_sammies:
    print("-" + sandwich)
    
