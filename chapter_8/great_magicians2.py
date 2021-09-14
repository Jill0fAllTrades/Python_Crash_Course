magicians = ['houdini', 'david copperfield', 'penn and teller']
great_magicians = [] #empty ending list

def show_magicians(names):
    print("Here are the magicians:")
    """prints the names of of each magician in magicians"""
    for name in names: 
        print("-" + name.title())
        
def make_great(magicians):
    print("\nAdds ")
    while magicians:
        current_magician = magicians.pop()
        print("-" + current_magician)
        great_magicians.append(current_magician + " the great!")       
        

show_magicians(magicians)

make_great(magicians)

print("\nHere's the list 'magicians':" + str(magicians))
print("\nHere's the list of great magicians!:" )
for magician in great_magicians:
    print("-" + magician)