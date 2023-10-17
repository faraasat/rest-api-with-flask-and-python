add = lambda x, y: x + y

print(add(5, 4))

print((lambda x, y: x + y)(5, 7))

sequence = [1, 2, 3, 4, 5]


def double(x):
    return x**2


doubled = [double(x) for x in sequence]

print(doubled)

doubled = map(double, sequence)

print(doubled)


doubled = [(lambda x: x * 2)(x) for x in sequence]

print(doubled)
