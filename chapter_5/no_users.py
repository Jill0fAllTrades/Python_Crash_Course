usernames = ['vibrittania', 'meowsforfood44', 'shuckadangdarn']

#
if usernames:
    for username in usernames:
            if username == 'admin':
                print("Hello admin, would you like to see a status report?")
            else:
                print("Hello, " + username + ", welcome back!")
else:
    print("Oh, no...")
