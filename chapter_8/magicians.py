magicians = ['houdini', 'david copperfield', 'penn and teller']

#TODO pass the list to a function called show magcicians
#TODO function prints the name of each magician in the list

def show_magicians(names):
    """prints the names of magicians"""
    for name in names:
        print(name.title())
    
show_magicians(magicians)    