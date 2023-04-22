"""
a="Hello World"
a.lower()
print(a)
a=5
b=6
total=a+b
print(total)
int_div=a/b
print(int_div)
comp=5 + 3j
print(comp.real)
print(comp.imag)
lst=['a','b','c']
print(lst)
lst.append(input())
for index, value in enumerate(lst):
    if value.islower() == True:
        lst[index] = value.upper()
print(lst)
user_details = {
    "name": "Naveen",
    "Email": "naveenjakher53@gmail.com"
}
print(user_details["name"])
print(user_details.get("class","Default"))
"""
def extend (lst, val):
    if type(val) is int:
        lst.append(val)
    else:
        lst.extend(val)
    return lst
