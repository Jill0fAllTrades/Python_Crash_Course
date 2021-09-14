# write a function called make_shirt
# accepts size and the text printed on the shirt
# it prints a sentence summarizing size of shirt and what will be printed on
#it
# call the function with positional arguments
# call the function with keyword arguments

def make_shirt(shirt_size, shirt_text):
    """prints the size of shirt and the text that will be printed on it"""
    print("You shirt will be a size " + shirt_size.upper() + " and will have "
          + "the following printed on it:\n\t" + shirt_text)
    
make_shirt(shirt_size = 's',shirt_text = 'shuckadangdarn')