magicians = ['houdini', 'david copperfield', 'penn and teller']

#TODO pass the list to a function called show magcicians
#TODO function prints the name of each magician in the list

def show_magicians(magicians):
    """prints the names of magicians"""
    for magician in magicians:
        print(magician.title())
    
    
show_magicians(magicians)
        
        
def make_great(magcicians):
    great_magicians = []
    for magician in magicians:
        great_magician = magician + ", the great"
        magicians.append(great_magician)
        print(magicians)
        
make_great(magicians)
show_magicians(magicians)        
        
    
