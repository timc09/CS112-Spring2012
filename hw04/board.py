'''
board.py
Tim Carroll
makes a checker board with user input
'''
height = int(raw_input("Height: "))
width = int(raw_input("Width: "))
temp = []
for y in range(height):
    for x in range(width):
        #even rows
        if y%2==0:
            #even columns
            if x%2==0:
                temp.append("#")
            #odd columns
            else:
                temp.append("-")
        #odd rows
        else:
            #even columns
            if x%2==0:#even columns
                temp.append("-")
            #odd columns
            else:
                temp.append("#")
    print "".join(temp)#converts list into string
    temp=[]#reset temp
