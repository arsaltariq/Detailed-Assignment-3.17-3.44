#Exercise 3.40:
#Splitting:

def partition(lst):
    for x in lst:
        x.casefold()
        if x[1] in "abcdefghijklm":
            print(x)
partition(['Eleanor', 'Evelyn', 'Sammy', 'Owen', 'Gavin'])
