from json import JSONEncoder

class Reimbursement:

    def __init__(self, username, r_id, amount, reason, status=None, manager_response=None):
        # Any parameters that we defined within our parameter are only in scope for this method.
        self._username = username
        self._r_id = r_id
        self._amount = amount
        self._reason = reason
        self._status = status
        self._manager_response = manager_response

    def get_username(self):
        return self._username

    def get_r_id(self):
        return self._r_id

    def get_amount(self):
        return self._amount

    def get_reason(self):
        return self._reason

    def get_status(self):
        return self._status

    def get_manager_response(self):
        return self.manager_response


class ReimbursementEncoder(JSONEncoder):
    def default(self, reimbursement):
        if isinstance(reimbursement, Reimbursement):
            return reimbursement.__dict__
        else:
            return super().default(self, reimbursement)

