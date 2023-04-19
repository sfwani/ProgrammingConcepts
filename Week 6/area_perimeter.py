'''
Description: This program creates a class to represent a regular polygon and calculates its perimeter and area using given formulae. It also prompts the user to input the number of sides and length of the polygon, performs input validation, and displays the dimensions of the polygon before calculating and displaying its perimeter and area.
'''

import math

class NSidedPolygon:
    def __init__(self):
        self.__n = 0
        self.__s = 0.0

    def set_n(self, n):
        self.__n = n

    def get_n(self):
        return self.__n

    def set_s(self, s):
        self.__s = s

    def get_s(self):
        return self.__s

    def perimeter(self):
        return self.__n * self.__s

    def area(self):
        return (self.__n * self.__s ** 2) / (4 * math.tan(math.pi / self.__n))

def main():
    polygon = NSidedPolygon()

    while True:
        n = int(input("Enter the number of sides (>=3): "))
        if n >= 3:
            break
        print("Invalid entry. Re-enter the number of sides (>=3).")

    while True:
        s = float(input("Enter the length of each side (>=0.1): "))
        if s >= 0.1:
            break
        print("Invalid entry. Re-enter the length of each side (>=0.1).")

    polygon.set_n(n)
    polygon.set_s(s)

    print("The polygon has {} sides. Each side is {:.3f} units in length.".format(polygon.get_n(), polygon.get_s()))
    print("The perimeter of the polygon is {:.3f} units and its area is {:.3f} square units.".format(polygon.perimeter(), polygon.area()))

if __name__ == '__main__':
    main()
