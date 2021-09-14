#ask user how many people are in their dinner group
#ig answer >8, say they'll have to wait for a table
#if any other answer, say your table is ready

seating = input("how many will be eating?")
seating = int(seating)

if seating >= 8:
    print("I'm sorry, you'll have to wait for a table.")
else:
    print("Your table is ready!")