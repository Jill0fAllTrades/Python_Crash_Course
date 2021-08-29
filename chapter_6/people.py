
person_0 = {'firstname': 'Brandon', 'lastname': 'Powers',
            'city': 'arlington heights'}

person_1 = {'firstname': 'Logyn', 'lastname': 'powers', 'city': 'jacksonville'}

person_2 = {'firstname': 'Lelouche', 'lastname': 'powers',
            'city': 'san diego'}

people = [person_0, person_1, person_2]
#TODOloop through list and print everything you know about each person organized

    
for person in people: #loops thru list people
    name = person['firstname'] + " " + person ['lastname']
    city = person['city']
    
    print(name.title() + " was born in " + city.title() + ".")