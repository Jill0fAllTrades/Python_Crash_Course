#make a dictionary called favorite places
fave_places = {
    'brandon': ['dc', 'tokyo'],
    'logyn': ['tokyo', 'los angeles'],
    'mom': ['arizona']
    }
#TODO loop thru dictionary and print name and fave place

for name, places in fave_places.items(): #loops thru values in fave_places
    print(name.title() + " loves the following cities: ")
    for place in places:
        print(place.title())