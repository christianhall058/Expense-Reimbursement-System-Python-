import unittest

from unittest.mock import Mock

import src.dao.employee_dao as ed

import src.service.employee_service as es
from app import flask_app


class EmployeeServiceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = flask_app.test_client()

    def setUp(self):
        self.app_context = flask_app.app_context()
        self.app_context.push()
        ed.get_user = Mock(return_value=('catman', 'catman', False, 'batman'))
        ed.get_r_id = Mock(return_value={})
        ed.reimburse_request = Mock(return_value=True)
        ed.get_reimbursements = Mock(return_value=[('catman', 2202, float('3432.00'), 'fjkdlsa', None, None), ('catman', 1651, float('3432.00'), 'fjkdlsa', None, None), ('catman', 9326, float('3432.00'), 'fjkdlsa', None, None), ('catman', 4180, float('3432.00'), 'fjkdlsa', None, None), ('catman', 1932, float('3432.00'), 'fjkdlsa', None, None), ('catman', 8118, float('789.00'), 'jfdsakhfkjvdshagihvdaskjnfk;das', None, None), ('catman', 1, float('100.00'), 'jdsfkhdashfuihasfpjkdjgjdskluuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', 'approve', 'No response'), ('catman', 2, float('17890.00'), 'something', 'approve', 'No response'), ('catman', 1034, float('3432.00'), 'fjkdlsa', 'approve', 'No response')])

    def test_get_user(self):
        username = 'catman'
        password = 'catman'
        expected_json = [{'true': 'e'}, 200]
        self.assertEqual(es.get_user(username, password).json, expected_json)

        ed.get_user = Mock(return_value=('batman', 'batman', True, None))
        username = 'batman'
        password = 'batman'
        expected_json = [{'true': 'm'}, 200]
        self.assertEqual(es.get_user(username, password).json, expected_json)

        password = ''
        self.assertEqual(es.get_user(username, password), ("false", 200))

        ed.get_user = Mock(return_value={})
        self.assertEqual(es.get_user(username, password), ("false", 200))

    def test_reimburse_request(self):
        username = 'catman'
        amount = '1233'
        reason = 'jdskaganglk'
        self.assertEqual(es.reimburse_request(username, amount, reason), ('true', 200))

    def test_get_reimbursements(self):
        username = 'catman'
        self.assertEqual(es.get_reimbursements(username), ('{"2202": {"_username": "catman", "_r_id": 2202, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "1651": {"_username": "catman", "_r_id": 1651, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "9326": {"_username": "catman", "_r_id": 9326, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "4180": {"_username": "catman", "_r_id": 4180, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "1932": {"_username": "catman", "_r_id": 1932, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "8118": {"_username": "catman", "_r_id": 8118, "_amount": 789.0, "_reason": "jfdsakhfkjvdshagihvdaskjnfk;das", "_status": null, "_manager_response": null}, "1": {"_username": "catman", "_r_id": 1, "_amount": 100.0, "_reason": "jdsfkhdashfuihasfpjkdjgjdskluuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", "_status": "approve", "_manager_response": "No response"}, "2": {"_username": "catman", "_r_id": 2, "_amount": 17890.0, "_reason": "something", "_status": "approve", "_manager_response": "No response"}, "1034": {"_username": "catman", "_r_id": 1034, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": "approve", "_manager_response": "No response"}}',200))

    def tearDown(self):
        self.app_context.pop()