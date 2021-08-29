
rivers_0 = {'Mississippi river': 'Mississippi',
            'Rio Grande': 'Colorado',
            'Hudson river': 'New York'}


for river, city in rivers_0.items():
    print("The " + river.title() + " runs through the state of " + city.title())


for river in rivers_0.keys():
    print(river)
#TODO loop to print the name of each country
for city in rivers_0.values():
    print(city)