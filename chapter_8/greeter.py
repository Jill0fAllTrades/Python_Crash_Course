def get_formatted_name(first_name, last_name):
    """return full name, neatly formatted"""
    full_name = first_name + '' + last_name
    return full_name.title()

while True:
    print("\nPlease tell me your name:")
    f_name = input("first_name:")
    l_name = input("last_name:")
    
formatted_name = get_formatted_name(f_name, l_name)
print("\nHello, " + formatted_name + "!")