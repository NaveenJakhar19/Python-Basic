
a="Hello, World!"
print(min(a))
#special character<num<uppercase<lowercase
print(max(a))

b="Hello1"
print(b.isalnum())
print(a.isalnum())

c="Hello"
print(c.isalpha())
print(a.isalpha())

d='hello '
print(d.islower())
print(a.islower())

e='HELLO'
print(e.isupper())
print(a.isupper())

f='     '
print(f.isspace())
print(a.isspace())

print(a.find('e',0,1))

print(f)
print(f.replace(" ","H",1))

print(a.split("e",1))
print(a.split("l",2))

g="Hello World!!"
print(g.partition("W"))

h="Hello"
print("*".join(h))

print(h.upper())

i="HELLO"
print(i.lower())

print(g.swapcase())

j="naveen jakhar"
print(j.capitalize())

k="Hello, World!"
print(k[1:13:-1])
