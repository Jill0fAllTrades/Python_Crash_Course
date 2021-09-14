def car_information(manufacturer, model, **car_info):
    """stores info about a car"""
    car = {}
    car['make'] = manufacturer
    car['model'] = model
    for key, value in car_info.items():
        car[key] = value
    return car

my_car = car_information('subaru', 'imprezza',
                         color = 'slate',
                         year = '2016',
                         tow_package=True)
print(my_car)