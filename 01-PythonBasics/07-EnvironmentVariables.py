import os

# print(os.environ)
# py_env = os.environ.get("MY_ENV")
environment = os.environ["environment"]
user = os.environ["user_api"]
password = os.environ.get("password_api")

# print(f"{py_user}, {py_password}, {py_env}")


def login(user, password):
    if user == "pycodebr" and password == "1234":
        return "Login Accepted"
    else:
        return "Login Denied"


def send_email():
    print("Email Log sent to the Admin")


# user = "pycodebr"
# password = "1234"

status = login(user, password)
print(status)

if environment == "dev":
    send_email()
