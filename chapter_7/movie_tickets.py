age = input("How old are you?\n")
age = int(age)

if age <= 3:
    print("Your ticket is free.")
elif age > 3 and age <= 12:
    print("Your ticket will cost $10.")
else:
    print("Your ticket will cost $15.")