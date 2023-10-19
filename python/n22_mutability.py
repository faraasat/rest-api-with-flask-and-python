# we are assigning reference
a = []
b = a

print(id(a), id(b))

a.append(35)

print(a, b)

b.append(45)

print(a, b)


c = 8597
d = 8597

print(id(c))
print(id(d))

c = 8598

print(id(c))
print(id(d))

e = "Hello"
f = e

print(e)
print(f)

e += " World"

print(e)
print(f)
