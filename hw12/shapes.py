from math import *
# Shapes
# =========================================================
# 
# Define a shape object.  This object has abstract (empty) 
# methods for calculating the area and perimeter of the 
# shape.
#
# After that, create classes for Rectangles, Squares, 
# and Circles.
# 
# When done, the code should work like this.
#     >>> r = Rect(3,4)
#     >>> print r.area()
#     12
#     >>> sq = Square(5)
#     >>> print sq.perimeter()
#     20
#     >>> print isinstance(sq, Rectangle)
#     True
#     >>> c = Circle(3)
#     >>> print c.area()
#     28.274333882308138
#     

class Shape(object):
    '''
    A shape.
    '''
    def __init__(self):
        pass
    
    def perimeter(self):
        pass

    def area(self):
        pass

class Rect(Shape):

    def __init__(self,width,height):
        self.width = width
        self.height = height

    def perimeter(self):
        return self.height*2 + self.width*2

    def area(self):
        return self.width*self.height

class Square(Rect):
    '''
    Square inherits from Rect
    '''
    def __init__(self,size):
        super(Square, self).__init__(size,size)

class Circle(Shape):
    '''
    Circle inherits from Shape
    '''
    def __init__(self, radius):
        self.radius = radius

    def perimeter(self):
        return 2*pi*self.radius

    def area(self):
        return pi*self.radius**2

def length(p1,p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def tri_area(p1,p2,p3):
    a = length(p1,p2)
    b = length(p1,p3)
    c = length(p2,p3)

    p = (a+b+c)/2.0

    return sqrt(p*(p-a)*(p-b)*(p-c))
    
    

class Polygon(Shape):
    '''
    Polgon inherits from Shape
    '''
    def __init__(self, *point_list):
        self.point_list = point_list
        self.pts = self.point_list
    
    def perimeter(self):
        total = 0
        for i in range(len(self.point_list)-1):
            total += length(self.point_list[i],self.point_list[i+1])
        total += length(self.point_list[-1],self.point_list[0])
        return total

    def area(self):
        p0 = self.point_list[0]
        total = 0
        for i in range(1,len(self.point_list)-1):
            p1 = self.point_list[i]
            p2 = self.point_list[i+1]
            total += tri_area(p0,p1,p2)
        return total


            
            
            

# Advanced Section
# ---------------------------------------------------------
# Add one more shape type: a polygon.  Polygons are created
# from a list of at least 3 points.
#
# >>> Polygon((0,0), (3,4), (0,4))
# >>> Polygon((0,0), (2,0), (2,2), (0,2))
#
# Perimeter should be easy to calculate, for area, use 
# method 1 on this site for finding the area of an irregular 
# polygon:
#   http://www.mathopenref.com/polygonirregulararea.html
# 
# You can find the area of a triangle with Heron's formula:
#   http://www.mathopenref.com/heronsformula.html
