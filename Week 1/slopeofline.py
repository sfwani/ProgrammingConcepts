'''
Description: this program asks user to enter the coordinates of two points 
which are then used to calculate the slope of the line connecting those two points.
'''

x1, y1 = input("Enter the coordinates (x,y) of point 1:\n(separated with a space)\n").split(sep=" ")
x1 = float(x1)
y1 = float(y1)

x2, y2 = input("Enter the coordinates (x,y) of point 2:\n(separated with a space)\n").split(sep=" ")
x2 = float(x2)
y2 = float(y2)

slope = (y2 - y1)/(x2-x1)

print(f"The slope of the line that connects two points {(x1, y1)} and {(y1, y2)} is", "{:.3f}".format(slope))

