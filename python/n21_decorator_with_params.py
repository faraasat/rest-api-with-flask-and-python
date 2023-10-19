import functools


# =====================================================
# ---------- Adding Parameters to Functions -----------
# =====================================================

user = {"username": "jose", "access_level": "admin"}


def make_secure(func):
    @functools.wraps(func)
    def secure_function(*args, **kwargs):
        if user["access_level"] == "admin":
            return func(*args, **kwargs)
        else:
            raise RuntimeError("User do not have this level of permission")

    return secure_function


@make_secure
def get_password2(panel):
    if panel == "admin":
        return "1234"
    elif panel == "billing":
        return "super_secure_password"


print(get_password2("billing"))

# =====================================================
# ---------- Adding Parameters to Decorator -----------
# =====================================================

# make_secure is a factory


def make_secure2(access_level):
    def decorator(func):
        @functools.wraps(func)
        def secure_function(*args, **kwargs):
            if user["access_level"] == access_level:
                return func(*args, **kwargs)
            else:
                return f"No {access_level} permission for {user['username']}"

        return secure_function

    return decorator


@make_secure2("admin")
def get_admin_password():
    return "1234"


@make_secure2("guest")
def get_dashboard_password():
    return "user: user_password"


print(get_admin_password())
print(get_dashboard_password())
