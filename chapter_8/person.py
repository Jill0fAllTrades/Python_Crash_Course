def build_person(first_name, last_name, age = ''):
    """return a dictionary of info about a person"""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', '27')
print(musician)

for item in musician.values():
    print(item.title())