# We had to import the JSONEncoder
from json import JSONEncoder

class Employee:

    def __init__(self, username, user_password, is_manager, manager_username):
        # Any parameters that we defined within our parameter are only in scope for this method.
        self._username = username
        self._user_password = user_password
        self._is_manager = is_manager
        self._manager_username = manager_username

    def get_username(self):
        return self._username

    def get_user_password(self):
        return self._user_password

    def get_is_manager(self):
        return self._is_manager

    def get_manager_username(self):
        return self._manager_username


class EmployeeEncoder(JSONEncoder):
    def default(self, employee):
        if isinstance(employee, Employee):
            return employee.__dict__
        else:
            return super().default(self, employee)

