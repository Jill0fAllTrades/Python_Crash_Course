
current_users = ['blueboy15', 'QackaducK', 'effyouStan', 'vibrittania',
                 'MeowsForFood44', 'shuckadangdarn']

new_users = ['ShmarmyPants22', 'qackaducK', 'shalomzzz', 'effyouStan',
             'SmellsOFWETSOCK']

#Check that a username has not already been used

current_users_lower = [user.lower() for user in current_users]

for user in new_users:
    if user.lower() in current_users_lower:
        print("Sorry, the username " + user.lower() + "is not available")
    else:
        print(user.lower() + "is available!")

