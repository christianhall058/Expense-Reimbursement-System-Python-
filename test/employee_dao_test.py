import unittest

from unittest.mock import Mock

import src.dao.employee_dao as ed

import src.service.employee_service as es
from src.utils import dbconfigs
from src.utils.dbconfigs import get_local_connection


class ManagerServiceTest(unittest.TestCase):

    def test_get_user(self):
        username = 'catman'
        conn = get_local_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("select * from employees where username= %s", [username, ])
            employee_data = cursor.fetchone()
            self.assertEqual(employee_data, ('catman', 'catman', False, 'batman'))
        finally:
            conn.close()

    def test_get_reimbursements(self):
        username = 'catman'
        conn = get_local_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("Select * from reimbursements where username = %s", [username, ])
            r_data = cursor.fetchall()
            self.assertEqual(str(r_data), "[('catman', 2, Decimal('17890.00'), 'something', None, None), ('catman', 1, Decimal('100.00'), 'jdsfkhdashfuihasfpjkdjgjdskluuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', 'approved', 'No response')]")
        finally:
            conn.close()

    def test_get_r_id(self):
        r_id = 2
        conn = get_local_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("Select * from reimbursements where r_id = %s", [r_id, ])
            r_data = cursor.fetchone()
            self.assertEqual(str(r_data), "('catman', 2, Decimal('17890.00'), 'something', None, None)")
        finally:
            conn.close()
