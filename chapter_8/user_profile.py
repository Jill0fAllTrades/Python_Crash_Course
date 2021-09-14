def build_profile(first,last, **user_info): #creates dictionary called user_info to pass info
    """Build a dictionart containing everything we know about a user."""
    profile = {} #empty dictionary named "profile" to store a users info
    profile['first name'] = first #stores 'first' parameter under key 'first name'
    profile['last name'] = last #stores 'last' parameter under key 'last name'
    for key, value in user_info.items(): #loops through key-value pairs in user_info
        profile[key] = value #adds them to the 'profile' dictionary
    return profile #returns that completed dictionary to call line


user_profile = build_profile('albert', 'einstein',  #stores returned 'profile' to 'user_profile'
                             location = 'princeton',
                             field = 'physics')
print(user_profile)

user_profile = build_profile('logyn', 'powers',
                             food = 'cheese',
                             location = 'newport news',
                             skin = 'brown')
print(user_profile)