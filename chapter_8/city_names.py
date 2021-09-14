#TODO write a function called city_country()

def city_country(city_name, country_name):
    """neatly formats a city, country"""
    formatted_city_country = city_name.title() + ', ' + country_name.title()
    return formatted_city_country


my_city = city_country('williamsburg', 'united states')
print("I live in " + my_city + ".")

dream_city = city_country('tokyo', 'japan')
print("I would love to visit " + dream_city + "!")

future_city = city_country('pristina', 'kosovo')
print("One day we may live in " + future_city + "...")