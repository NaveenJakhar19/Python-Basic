# To print no. of those string whose first and last element is same in a list.\

#Declaring a empty list.
list = []

#Taking length of list.
a=int(input("Enter the length of list:"))

#Taking input of elements of list.
for i in range(a):
    x=str(input("Enter the string: "))
    list.append(x)

#Taking no. of strings whose first and last letter is same.
n=0
for word in list:
    a=len(word)
    if word[0]==word[a-1]:
        n=n+1

#Printing the result.
print("There are ",n," no. of strings with same first and last element.")