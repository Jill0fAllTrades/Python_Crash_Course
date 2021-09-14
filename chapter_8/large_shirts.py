def make_shirt(shirt_size = 'L', shirt_text = "I love Python!"):
    """prints the size of shirt and the text that will be printed on it"""
    print("You shirt will be a size " + shirt_size.upper() + " and will have "
          + "the following printed on it:\n\t" + shirt_text)
    
make_shirt(shirt_size = 'M', shirt_text = "Wow wow wee wow")