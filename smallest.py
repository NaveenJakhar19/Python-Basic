a=int(input("Enter the length of list:"))
list = []
for i in range(a):
    x=int(input("Enter the element:"))
    list.append(x)
print(list)
b=list[0]
for j in list:
    if b>j :
        b=j
print(b," is the smallest no.")