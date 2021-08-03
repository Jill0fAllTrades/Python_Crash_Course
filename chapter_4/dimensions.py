#define the tuple with () instead of []
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)
    
dimensions = (500, 100, )
print("New dimensions:")
for dimension in dimensions:
    print(dimension)