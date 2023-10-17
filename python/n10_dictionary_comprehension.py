users = [
    (0, "Bob", "pa$$"),
    (1, "Anne", "Pasdf"),
    (2, "Rolf", "sad"),
    (3, "User", "bili"),
]

username_mapping = {user[1]: user for user in users}

print(username_mapping)
