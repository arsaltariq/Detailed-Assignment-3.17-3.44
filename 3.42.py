#Exercise 3.42:
#Function Average:

def avg(multiList):
    sum=0
    for x in multiList:
        tmpLst=x
        for i in tmpLst:
            sum+=i        
        print(sum/len(tmpLst))
        sum =0

multiList=[[95, 92, 86, 87], [66, 54], [89, 72, 100], [33, 0, 0]]
avg(multiList)
