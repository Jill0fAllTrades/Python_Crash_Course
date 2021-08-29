#make a dictionary called 'cities'
cities = {
    'tokyo': {'country': 'japan',
              'population': '13.96 million',
              'fact': 'most populous metropolitan area'},
    'pristina': {'country': 'kosovo',
                 'population': '1.86 million',
                 'fact': 'more than 40% of the population is under 25'},
    'seoul': {'country': 'korea',
              'population': '9.7 million',
              'fact': 'more than half of koreas population lives in seoul'}
    }


#print the name of each city and all the info neatly
for city, facts in cities.items():
        country = facts['country']
        pop = facts['population']
        fact = facts['fact']
        print(city.title() + ": " + "\n" + "Located in " + country.title() +
              ", with a population of " + pop + "." + "\n" + "Fun fact: " +
              fact + "!")
