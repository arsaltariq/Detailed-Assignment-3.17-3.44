#Exercise 3.29:
#Requesting a positive integer and printing all the positive divisors:

n=eval(input("Enter a positive integer n :"))
for i in range(1,n+1):
    if(n%i==0):
        print(i)
