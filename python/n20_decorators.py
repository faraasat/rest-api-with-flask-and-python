import functools

user = {"username": "jose", "access_level": "admin"}

# =====================================================
# ------------------- DEC 1 ---------------------------
# =====================================================


def make_secure(func):
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            raise RuntimeError("User do not have this level of permission")

    return secure_function


def get_admin_password():
    return "1234"


get_admin_password = make_secure(get_admin_password)

print(get_admin_password())

# =====================================================
# ------------------- DEC 2 ---------------------------
# =====================================================


@make_secure
def get_admin_password2():
    return "1234"


# using at operator with decorators make function loose its name and documenation
print(get_admin_password2.__name__)
print(get_admin_password2())


# =====================================================
# ------------------- DEC 3 ---------------------------
# =====================================================

user = {"username": "jose", "access_level": "guest"}


def make_secure2(func):
    @functools.wraps(func)
    def secure_function():
        if user["access_level"] == "admin":
            return func()
        else:
            raise RuntimeError("User do not have this level of permission")

    return secure_function


@make_secure2
def get_admin_password3():
    return "1234"


print(get_admin_password3.__name__)
print(get_admin_password3())
