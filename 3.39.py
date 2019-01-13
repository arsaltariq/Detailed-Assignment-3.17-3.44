#Exercise 3.39:
#True and false taking six arguments:

def collision(x1,y1,r1,x2,y2,r2):
    if(((x2-x1)**2+(y2-y1)**2)<(r1+r2)**2):
        print(True)
    else:
        print(False)
collision(0,0,3,0,5,3)
collision(0,0,1.4,2,2,1.4)
