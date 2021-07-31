from flask import jsonify
from werkzeug.utils import redirect
from json import dumps

import src.dao.manager_dao as mdao
from src.models.Reimbursement import Reimbursement, ReimbursementEncoder
from src.models.employee import Employee
import logging

logging.basicConfig(filename='All.log', level=logging.INFO)

def get_reimbursements():
    try:
        r_data = mdao.get_reimbursements()
        logging.info("The r_data sent back is: " + str(r_data))
        r_dict = {}
        for r in r_data:
            r_dict[r[1]] = Reimbursement(r[0], r[1], float(r[2]), r[3], r[4], r[5])
            logging.info("r_dict[" + str(r[1]) + "] = username: " + r[0] + " and r_id: " + str(r[1]) + " and amount: " + str(r[2]) + " and reason: " + r[3] + " and status: " +str(r[4])+ " and manager response: "+str(r[5]))

        my_json = dumps(r_dict, cls=ReimbursementEncoder)
        logging.info("This is what is returned" + str(my_json))
        return my_json, 200

    except Exception as e:
        logging.exception('Unexpected server error')


def approve_reimbursement(r_id, r_status, manager_response):
    try:
        return mdao.approve_reimbursement(r_id, r_status, manager_response)
    except Exception as e:
        logging.exception('Unexpected server error')

def get_statistics():
    try:
        r_data = mdao.get_reimbursements()
        logging.info("The r_data sent back is: " + str(r_data))
        r_dict = {}
        usernames = {}
        greatest_amount = 0
        greatest_spender = ""
        greatest_spender_amount = 0
        total_amount = 0
        total_reimbursements = 0
        for r in r_data:
            r_dict[r[1]] = Reimbursement(r[0], r[1], float(r[2]), r[3], r[4], r[5])
            logging.info("r_dict[" + str(r[1]) + "] = username: " + r[0] + " and r_id: " + str(r[1]) + " and amount: " + str(r[2]) + " and reason: " + r[3] + " and status: " + str(r[4]) + " and manager response: " + str(r[5]))

        for r_id in r_dict:
            #get the username
            username = r_dict[r_id].get_username()

            #check to see if the username is used
            if username not in usernames:
                usernames[username] = 0

            #add up the amounts of each user
            usernames[username] += r_dict[r_id].get_amount()

            #find the greatest amount spent
            if r_dict[r_id].get_amount() > greatest_amount:
                greatest_amount = r_dict[r_id].get_amount()

            #get totals for average
            total_amount += r_dict[r_id].get_amount()
            total_reimbursements += 1

        average_amount = total_amount/total_reimbursements
        logging.info("average amount: "+str(average_amount)+", total amount: "+str(total_amount)+", total reimbursements: "+str(total_reimbursements))

        # rerun the loop
        for r_id in r_dict:
            username = r_dict[r_id].get_username()
            #find the greatest_spender
            if usernames[username] > greatest_spender_amount:
                greatest_spender_amount = usernames[username]
                greatest_spender = username

        logging.info("greatest spender: "+greatest_spender+", greatest spender amount: "+str(greatest_spender_amount))

        statistics = {
            "greatest_amount": greatest_amount,
            "greatest_spender": greatest_spender,
            "greatest_spender_amount": greatest_spender_amount,
            "total_amount":total_amount,
            "total_reimbursements":total_reimbursements
        }

        return jsonify(statistics)

    except Exception as e:
        logging.exception('Unexpected server error')