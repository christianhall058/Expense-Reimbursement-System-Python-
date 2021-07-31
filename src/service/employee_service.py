# We need to import our user_dao so that we can access the functions
from random import seed, randint

from flask import make_response, jsonify
from werkzeug.utils import redirect
from json import dumps

import src.dao.employee_dao as edao
from src.models.Reimbursement import Reimbursement, ReimbursementEncoder
from src.models.employee import Employee

import logging

logging.basicConfig(filename='All.log', level=logging.INFO)

def get_user(username, password):
    try:
        user = edao.get_user(username)
        logging.info("This is what get user returned: " + str(user))

        if not user:
            logging.info("This user did not exist")
            return "false", 200
        employee = Employee(user[0], user[1], user[2], user[3])
        logging.info("employee is username: " + employee.get_username() + ", password: " + employee.get_user_password() + ", is_manager: " + str(employee.get_is_manager()) + ", manager_username: " + str(employee.get_manager_username()))

        if password != employee.get_user_password():
            logging.info("This password does not match")
            return "false", 200

        if employee.get_is_manager():
            logging.info("employee is manager")
            return jsonify({True: "m"}, 200)
        else:
            logging.info("employee is not a manager")
            return jsonify({True: "e"}, 200)

    except Exception as e:
        logging.exception('Unexpected server error')

def reimburse_request(username, amount, reason):
    try:
        seed(1)
        while True:
            r_id = randint(1, 10000)
            if not edao.get_r_id(r_id):
                logging.info("The r_id is: " + str(r_id))
                break

        edao.reimburse_request(username, r_id, amount, reason)
        logging.info("Request sent successfully")
        return "true", 200
    except Exception as e:
        logging.exception('Unexpected server error')


def get_reimbursements(username):
    try:
        r_data = edao.get_reimbursements(username)
        logging.info("The r_data sent back is: " +str(r_data))
        r_dict = {}
        for r in r_data:
            r_dict[r[1]] = Reimbursement(r[0], r[1], float(r[2]), r[3], r[4], r[5])
            logging.info("r_dict["+str(r[1])+"] = username: "+r[0]+" and r_id: "+str(r[1])+ " and amount: "+str(r[2])+ " and reason: "+r[3]+ " and status: "+str(r[4]) + " and manager response: "+str(r[5]))

        my_json = dumps(r_dict, cls=ReimbursementEncoder)
        logging.info("This is what is returned"+str(my_json))
        return my_json, 200
    except Exception as e:
        logging.exception('Unexpected server error')