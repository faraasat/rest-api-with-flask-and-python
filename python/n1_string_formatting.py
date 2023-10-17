name = "Bob"

greetings1 = f"Hello {name}"

# this allows us to define the value multiple times (template)
greetingsTemplate = "Hello {} !!"
greetings2 = greetingsTemplate.format(name)

print(greetings1)
print(greetings2)
