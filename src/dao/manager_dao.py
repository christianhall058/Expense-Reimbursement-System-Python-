from src.utils.dbconfigs import get_connection


def get_reimbursements():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("select * from reimbursements")
        r_data = cursor.fetchall()
        return r_data
    finally:
        conn.close()


def approve_reimbursement(r_id, r_status, manager_response):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("Update reimbursements set status = %s, manager_response = %s where r_id = %s", [r_status, manager_response, r_id])
        conn.commit()
        return "true", 200
    finally:
        conn.close()