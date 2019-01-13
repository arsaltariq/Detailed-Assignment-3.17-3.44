#Exercise 3.37:
#Computing slope of line and distance between two points:

import math
def points(x1,y1,x2,y2):
    slope=(y2-y1)/(x2-x1)
    distance=math.sqrt((x2-x1)**2+(y2-y1)**2)
    print("The Slope is : ",slope," The distance is : ",distance)
points(0,0,1,1)
