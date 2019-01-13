#Exercise 3.43:
#x and y coordinates for center and the radius of the circle:

def hit(x1,y1,r,x2,y2):
    if(((x2-x1)**2+(y2-y1)**2)<=r**2):
       print(True)
    else:
       print(False)
hit(0,0,3,3,0)
hit(0,0,3,4,0)
