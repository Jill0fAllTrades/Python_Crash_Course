#TODO use a list comprehension to generate a list of first 10 cubes

cubelist = list(range(1,10))

cubes = [value**3 for value in cubelist]

for cube in cubes:
    print(cube)