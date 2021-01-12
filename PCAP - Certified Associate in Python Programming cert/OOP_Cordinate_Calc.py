"""
This is how we imagine the class:

it's called Point;
its constructor accepts two arguments (x and y respectively), both default to zero;
all the properties should be private;
the class contains two parameterless methods called getx() and gety(), which return each of the two coordinates (the coordinates are stored privately, so they cannot be accessed directly from within the object);
the class provides a method called distance_from_xy(x,y), which calculates and returns the distance between the point stored inside the object and the other point given as a pair of floats;
the class provides a method called distance_from_point(point), which calculates the distance (like the previous method), but the other point's location is given as another Point class object;

"""

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

point1 = Point(0, 0)
point2 = Point(1, 1)

print(point1.distance_from_point(point2))
print(point2.distance_from_xy(2, 0))
