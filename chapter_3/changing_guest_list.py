#list/array of the deceased
guests = ['abe lincoln', 'tupac', 'biggie', 'lavonne']

#print a message to each person, iviting them to dinner
message = ("Dear, " + guests[1].title() + ", wanna get some noms?!")
print(message)
#replace the name of the guest who is a no show with name of new person
popped_guest = guests.pop(-1)

guests.append('princess')
#
print("Unfortunately, " + popped_guest.title() + " won't be joining us.")

message1 = ("Dear, " + guests[0].title() + ", wanna get some noms?!")
message2 = ("Dear, " + guests[1].title() + ", wanna get some noms?!")
message3 = ("Dear, " + guests[2].title() + ", wanna get some noms?!")

print("Dear, " + str(guests) + ", " + guests[1] + ", " + guests[2] + ", we have a bigger table!")

guests.insert(0, 'Lexi')
guests.insert(2, 'grandma Brown')
guests.append('Felix')

popped_guest1 = guests.pop()
print("Sorry, " + popped_guest1)
popped_guest2 = guests.pop()
print("Sorry, " + popped_guest2)
popped_guest3 = guests.pop()
print("Sorry, " + popped_guest3)

print(guests)

del guests[0]
del guests[0]
del guests[0]
del guests[0]

print(guests)