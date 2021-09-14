magicians = ['houdini', 'david copperfield', 'penn and teller']
great_magicians = [] #empty ending list

def show_magicians(names):
    print("Here are the magicians:")
    """prints the names of of each magician in magicians"""
    for name in names: 
        print("-" + name.title())
        
def make_great(magicians):
    """Adds "the great" to the end of each magician in magicians"""
    while magicians: #while there are names in the magicians list...
        current_magician = magicians.pop() #pop off last name & store it in current
        print("-" + current_magician) #print it
        great_magicians.append(current_magician + " the great!")       
        #lastly, add that stored variable to my new list + 'the great'

show_magicians(magicians)

make_great(magicians[:])

print("\nHere's the list 'magicians':" + str(magicians))
print("\nHere's the list of great magicians!:" )
for magician in great_magicians:
    print("-" + magician)