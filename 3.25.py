#Exercise 3.25:
#Requesting a list then printing certain names:

word_list=eval(input("Enter the list of names:"))
for i in word_list:
    i.casefold()
    if i[1] in "abcdefghijklm":
        print(i)
