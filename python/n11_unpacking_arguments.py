def multiply(*args):
    res = 1
    for m in args:
        res *= m
    return res


def sum(*args):
    res = 0
    for m in args:
        res += m
    return res


def add(x, y):
    return x + y


print(multiply(1, 6, 8, 23))


nums = [5, 6]

print(add(*nums))

nums = {"x": 5, "y": 6}
# ** pass it as named arguments it will pass like x=5, y=6
print(add(**nums))


def apply(*args, operator):
    if operator == "*":
        return multiply(*args)
    elif operator == "+":
        return sum(*args)
    else:
        return "no valid operator"


print(apply(1, 2, 3, 4, 5, operator="*"))


# keyword arguments
def named(**kwargs):
    print(kwargs)


user = {"name": "Bob", "age": 78}

named(**user)


def named2(name, age):
    print(name, age)


named2(**user)
