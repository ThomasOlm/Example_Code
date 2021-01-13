## Using the cordinate plan class to calculate the perimeter of a triangle 

import math


class Point:

    def __init__(self, x=0.0, y=0.0):

        self.__y = y
        self.__x = x

    def getx(self):

        return self.__x

    def gety(self):

        return self.__y

    def distance_from_xy(self, x, y):

        __hypo_x = 0.0
        __hypo_y = 0.0

        if x > self.__x:

            __hypo_x = x - self.__x

        else:

            __hypo_x = self.__x - x

        if y > self.__y:

            __hypo_y = y - self.__y

        else:

            __hypo_y = self.__y - y

        return math.hypot(__hypo_x, __hypo_y)

    def distance_from_point(self, point):

        return self.distance_from_xy(point.getx(), point.gety())

class Triangle:

    def __init__(self, vertice1, vertice2, vertice3):
        
        self.side1 = vertice1.distance_from_point(vertice2)

        self.side2 = vertice1.distance_from_point(vertice3)

        self.side3 = vertice2.distance_from_point(vertice3)

    def perimeter(self):
        
        return self.side1 + self.side2 + self.side3

triangle = Triangle(Point(0, 0), Point(1, 0), Point(0, 1))
print(triangle.perimeter())
