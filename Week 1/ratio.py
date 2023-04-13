''' 
Description: the program asks for the number of spheres to be put inside a cylinderical container
and also asks for the diameter of each sphere. It then calculates the volume of the spheres and the cylinder
and takes their ratio and prints it to the screen.
'''

import math

spheres = int(input("Enter the number of spheres to be placed in the container:\n"))
diameter = float(input("Enter the diameter of each sphere (in inches):\n"))

height = spheres*diameter

print(f"The container would need to be at least {height} inches to hold the {spheres} spheres.")

pi = math.pi
radius = diameter/2
volumeOfSphere = (4*pi*radius**3)/3
volumeOfCylinder = height*pi*radius**2

ratio = (spheres*volumeOfSphere/volumeOfCylinder)*100

print(f"The {spheres} spheres will occupy", "{:.2f}%".format(ratio),"of the container." )
