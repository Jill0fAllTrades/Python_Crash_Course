pet_0 = {'name': 'lelouche','species': 'cat', 'owner': 'logyn'}

pet_1 = {'name': 'gouda', 'species': 'cat', 'owner': 'brandon'}

pet_2 = {'name': 'weenalina', 'species': 'dog', 'owner': 'landyn'}

pets = [pet_0, pet_1, pet_2]

for pet in pets:
    name = pet['name']
    type = pet['species']
    
    print(name.title() + " is a " + type + ".")