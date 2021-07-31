import json

from werkzeug.utils import redirect

from app import flask_app

from flask import jsonify, render_template, make_response, request

import werkzeug.exceptions

import logging

from flask_cors import CORS, cross_origin

from src.service import employee_service, manager_service

logging.basicConfig(filename='All.log', level=logging.INFO)


@flask_app.route('/login', methods=['GET'])
def hello_world():
    return render_template("login.html")


@flask_app.route('/employee/<username>', methods=['GET'])
def employee_page(username):
    return render_template("employeePage.html")


@flask_app.route('/manager/<username>', methods=['GET'])
def manager_page(username):
    return render_template("managerPage.html")


@flask_app.route('/employee/<username>/reimburse_request', methods=['GET'])
def reimbursement_request_page(username):
    return render_template("r_request_page.html")


@flask_app.route('/employee/<username>/past_requests', methods=['GET'])
def past_request_page(username):
    return render_template("past_requests.html")


@flask_app.route('/findEmployee', methods=['POST'])
def get_user():
    raw_data = request.data.decode('UTF-8')
    data = json.loads(raw_data)
    username = data.get('username')
    password = data.get('password')

    return employee_service.get_user(username, password)


@flask_app.route('/employee/<username>/reimburse_request/form', methods=['POST'])
def reimburse_request(username):
    raw_data = request.data.decode('UTF-8')
    data = json.loads(raw_data)
    amount = data.get('amount')
    reason = data.get('reason')

    return employee_service.reimburse_request(username, amount, reason)


@flask_app.route('/employee/<username>/reimbursements', methods=['GET'])
def get_reimbursements(username):
    return employee_service.get_reimbursements(username)


















@flask_app.route('/manager/<username>/reimbursement_view', methods=['GET'])
def reimbursement_view(username):
    return render_template("manager_r_view.html")


@flask_app.route('/manager/<username>/statistics', methods=['GET'])
def statistics_view(username):
    return render_template("statistics.html")


@flask_app.route('/manager/<username>/get_statistics', methods=['GET'])
def get_statistics(username):
    return manager_service.get_statistics()


@flask_app.route('/manager/<username>/get_reimbursements', methods=['GET'])
def m_get_reimbursements(username):
    return manager_service.get_reimbursements()


@flask_app.route('/manager/<username>/approve_reimbursements', methods=['PUT'])
def approve_reimbursement(username):
    raw_data = request.data.decode('UTF-8')
    data = json.loads(raw_data)
    r_id = data.get('r_id')
    r_status = data.get('r_status')
    manager_response = data.get('manager_response')

    return manager_service.approve_reimbursement(r_id, r_status, manager_response)


