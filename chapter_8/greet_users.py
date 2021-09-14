def greet_users(names):
    """greets users by name"""
    for name in names:
        msg = "Hello, " + name.title() + "!"
        print(msg)
        
usernames = ['logyn', 'landyn', 'elijah']
greet_users(usernames)