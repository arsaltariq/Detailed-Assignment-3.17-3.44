#Exercise 3.34:
#Taking two arguments and computing pay:

x=eval(input("Enter your hourly wage:"))
y=eval(input("Enter number of hours:"))
sum=0
def pay(x,y):
    if y<40:
        sum=x*y
    else:
        sum=x*40
        sum+=(x*1.5)*(y-40)
       
    return sum
pay(10,35)
pay(10,45)
