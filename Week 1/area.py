'''
Description: this code asks the user for the radius of a flower
which is then put into different formulas to calculate the total
area of the circle.
'''

radiusOfFlower = float(input("What's the radius of the flower?\n(press enter after writing the value)\n"))

sideOfSquare = radiusOfFlower
areaOfSquare = sideOfSquare*sideOfSquare
print("Area of the square part of the flower:", areaOfSquare)

pi = 3.14159
radiusOfCircle = radiusOfFlower/2
areaOfCircles = 2*pi*radiusOfCircle**2
print("Area of circular parts of the flower:", areaOfCircles)

areaOfFlower = areaOfCircles + areaOfSquare
print("Total Area of the flower:", areaOfFlower)