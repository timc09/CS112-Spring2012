from math import *
# Point Object
# =====================================
# Create a Point point class.  Point objects, when created, look like this:
#     >>> pt = Point(3,4)
#     >>> print pt.x
#     3
#     >>> print pt.y
#     4
#
# In addition points have the following methods:
#    distance(self, other):
#        calculates the distance between this point and another
#    
#    move(self, x, y):
#        sets the points location to x,y
# 
#    translate(self, x, y):
#        offsets the point by x and y
# 
#    When all done, points should work like this:
#
#    >>> a = Point(0,0)
#    >>> b = Point(0,0)
#    >>> b.move(2, 2)
#    >>> print b.x, b.y
#    2 2
#    >>> b.translate(1,2)
#    >>> print b.x, b.y
#    3 4
#    >>> print a.distance(b)
#    5
#
class Point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def distance(self,other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

    def move(self,x,y):
        self.x = x
        self.y = y

    def translate(self, x, y):
        self.x = self.x + x
        self.y = self.y + y

    def slope(self,other):
        m = 0
        dx = self.x - other.x
        dy = self.y - other.y
        if dx != 0:
            m = float(dy)/dx
        else:
            m = None
        return m

    def extrapolate(self,m,dist):
        if m is not None:
            theta = atan(m)
            y = sin(theta)*dist + self.y
            x = cos(theta)*dist + self.x
        else:
            x = self.x
            y = self.y + dist
        return(Point(x,y))
    
    def __eq__(self,other):
        return isinstance(other, Point) and other.x == self.x and other.y == self.y 
        
    def __str__(self):
        return '('+str(self.x)+','+str(self.y)+')'

# Advanced Section:
# ---------------------------------------
# Add the following function:
#     slope(self, other):
#         calculate the slope between two points
#
#     extrapolate(self, slope, distance):
#         returns a point along the line defined by slope
#         a given distance away
#
# Also, add the following special python methods:
#     __eq__(self, other):
#         checks if other is a Point and is equal to self
#
#     __str__(self):
#         returns a string representation of the point 
#     
#     >>> print Point(3,4)
#     (3,4)
#     >>> a = Point(1,2)
#     >>> b = Point(1,2)
#     >>> print a == b
#     True
