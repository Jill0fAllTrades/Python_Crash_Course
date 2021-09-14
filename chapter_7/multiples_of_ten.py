#ask user for a number
number = input("Give me a number " +
               "and I'll tell you if it's a multiple of ten!:\n")
number = int(number)

#TODO report whether the number is a multple of 10 or not
if number % 10 == 0:
    print(str(number) + " is a multiple of 10!")
else:
    print(str(number) + " is not divisible by 10.")