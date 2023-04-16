'''
Description: the uses the turtle module to create a graphical representation of a polygon. 
program asks the user for the number of sides and the length of each side of the polygon.
program then calculates the interior angle of the polygon
it then sends intructions to the turle module to draw the polygon and print the name of the polygon on screen
the names of the polygons are printed using an if else statement
'''

import turtle

sanaan = turtle.Turtle()

numberOfSides = turtle.numinput('Side Entry','Enter the number of sides', default = 3, minval = 3, maxval = 12)
lengthOfSides = turtle.numinput('Length Entry','Enter the length of each side', default = 50, minval = 50, maxval = 250)

angle = 180 * (numberOfSides - 2)/numberOfSides

turnAngle = 180 - angle

for i in range(int(numberOfSides)):
    sanaan.forward(lengthOfSides)
    sanaan.left(turnAngle)

if numberOfSides == 3:
    polygonName = "Triangle"
elif numberOfSides == 4:
    polygonName = "Quadrilateral"
elif numberOfSides == 5:
    polygonName = "Pentagon"
elif numberOfSides == 6:
    polygonName = "Hexagon"
elif numberOfSides == 7:
    polygonName = "Heptagon"
elif numberOfSides == 8:
    polygonName = "Octagon"
elif numberOfSides == 9:
    polygonName = "Nonagon"
elif numberOfSides == 10:
    polygonName = "Decagon"
elif numberOfSides == 11:
    polygonName = "Hendecagon"
elif numberOfSides == 12:
    polygonName = "Dodecagon"

sanaan.penup()
sanaan.backward(75)
sanaan.write(polygonName, align="center", font=("Arial", 15, "normal"))
sanaan.hideturtle()

turtle.done()

