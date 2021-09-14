#alien was just shot down.
alien_color = 'red'

#if statement to test whethert aliens color is green
if alien_color == 'green':
    points = 5
elif alien_color is 'yellow':
    points = 10
elif alien_color is 'red':
    points = 15
else:
    points = 0
    
    
print("You just earned " + str(points) + " points!")