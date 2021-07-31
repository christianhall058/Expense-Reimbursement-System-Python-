import unittest

from unittest.mock import Mock

import src.dao.manager_dao as md

import src.service.manager_service as ms
from src.utils.dbconfigs import get_local_connection


class ManagerServiceTest(unittest.TestCase):

    def test_get_reimbursements(self):
        conn = get_local_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("select * from reimbursements")
            r_data = cursor.fetchall()
            self.assertEqual(str(r_data), "[('catman', 2, Decimal('17890.00'), 'something', None, None), ('catman', 1, Decimal('100.00'), 'jdsfkhdashfuihasfpjkdjgjdskluuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuuu', 'approved', 'No response')]")
        finally:
            conn.close()