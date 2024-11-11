import os

py_env = os.environ.get('MY_ENV')
py_user = os.environ.get('MY_USER')
py_password = os.environ.get('MY_PASSWORD')

print(f'{py_user}, {py_password}, {py_env}')
