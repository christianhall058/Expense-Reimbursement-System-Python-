# We need to import our module for establishing a connection to the DB
from src.utils.dbconfigs import get_connection


def get_user(username):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("select * from employees where username= %s", [username, ])
        employee_data = cursor.fetchone()
        return employee_data
    finally:
        conn.close()

def reimburse_request(username, r_id, amount, reason):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("Insert into reimbursements(username, r_id, amount, reason) values(%s, %s, %s, %s)", [username, r_id, amount, reason])
        conn.commit()
        return True
    finally:
        conn.close()

def get_reimbursements(username):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("Select * from reimbursements where username = %s", [username, ])
        r_data = cursor.fetchall()
        return r_data
    finally:
        conn.close()

def get_r_id(r_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("Select * from reimbursements where r_id = %s", [r_id, ])
        r_data = cursor.fetchone()
        return r_data
    finally:
        conn.close()