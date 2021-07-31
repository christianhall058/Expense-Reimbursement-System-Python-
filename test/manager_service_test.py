import unittest

from unittest.mock import Mock

import src.dao.manager_dao as md

import src.service.manager_service as ms
from app import flask_app


class ManagerServiceTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = flask_app.test_client()

    def setUp(self):
        self.app_context = flask_app.app_context()
        self.app_context.push()
        md.get_reimbursements = Mock(return_value=[('catman', 2202, float('3432.00'), 'fjkdlsa', None, None), ('catman', 1651, float('3432.00'), 'fjkdlsa', None, None), ('catman', 9326, float('3432.00'), 'fjkdlsa', None, None), ('catman', 4180, float('3432.00'), 'fjkdlsa', None, None), ('catman', 1932, float('3432.00'), 'fjkdlsa', None, None), ('catman', 8118, float('789.00'), 'jfdsakhfkjvdshagihvdaskjnfk;das', None, None), ('catman', 1, float('100.00'), 'jdsfkhdashfuihasfpjkdjgjdskluuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', 'approve', 'No response'), ('catman', 2, float('17890.00'), 'something', 'approve', 'No response'), ('catman', 1034, float('3432.00'), 'fjkdlsa', 'approve', 'No response')])
        md.approve_reimbursement = Mock(return_value=True)

    def test_get_reimbursements(self):
        self.assertEqual(ms.get_reimbursements(), ('{"2202": {"_username": "catman", "_r_id": 2202, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "1651": {"_username": "catman", "_r_id": 1651, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "9326": {"_username": "catman", "_r_id": 9326, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "4180": {"_username": "catman", "_r_id": 4180, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "1932": {"_username": "catman", "_r_id": 1932, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": null, "_manager_response": null}, "8118": {"_username": "catman", "_r_id": 8118, "_amount": 789.0, "_reason": "jfdsakhfkjvdshagihvdaskjnfk;das", "_status": null, "_manager_response": null}, "1": {"_username": "catman", "_r_id": 1, "_amount": 100.0, "_reason": "jdsfkhdashfuihasfpjkdjgjdskluuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu", "_status": "approve", "_manager_response": "No response"}, "2": {"_username": "catman", "_r_id": 2, "_amount": 17890.0, "_reason": "something", "_status": "approve", "_manager_response": "No response"}, "1034": {"_username": "catman", "_r_id": 1034, "_amount": 3432.0, "_reason": "fjkdlsa", "_status": "approve", "_manager_response": "No response"}}',200))

    def test_approve_reimbursement(self):
        r_id = 134
        status = 'approved'
        manager_response = 'fdjskfla;'
        self.assertEqual(ms.approve_reimbursement(r_id, status, manager_response), True)

    def test_get_statistics(self):
        self.assertEqual(ms.get_statistics().json, {'greatest_amount': 17890.0, 'greatest_spender': 'catman', 'greatest_spender_amount': 39371.0, 'total_amount': 39371.0, 'total_reimbursements': 9})

    def tearDown(self):
        self.app_context.pop()