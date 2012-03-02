#!/usr/bin/python env

# Calculate if a point is within a box
#    check if a point is inside a given box.  
#
#    Parameters:
#       pt: list of 2 numbers (x,y)
#       box: list of 4 numbers (x,y,w,h).  x,y is the top left point.  w,h is the width and height

def point_in_box(pt, box):
    print pt
    print box
    x = pt[0]
    y = pt[1]
    top = box[0]
    left = box[1]
    right = box[0]+box[2]
    bot = box[1]+box[3]

    print x,y,top,bot,left,right
    if x >= left and x < right:
        if y < bot and y >= top:
            print 'true'
            return True
        else:
            print 'F'
            return False
    else:
        print left,'<',x,'<'
        print 'Fals'
        return False
    
