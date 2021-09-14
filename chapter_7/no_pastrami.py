#make a list and fill it with names of sandwiches
sammies = ['reuben', 'pastrami', 'monte cristo', 'BLT', 'lox bagel',
           'grilled cheese', 'pastrami', 'pastrami', ]

#empy list called finished sandwiches
finished_sammies = []

print("The deli has run out of Pastrami. Sorry for the inconvenience.\n")
while 'pastrami' in sammies:
    sammies.remove('pastrami')

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
    
