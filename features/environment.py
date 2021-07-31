from selenium import webdriver
from selenium_content.poms.login_page import LoginPage
from selenium_content.poms.employee_page import EmployeePage
from selenium_content.poms.manager_page import ManagerPage
from selenium_content.poms.employee_reimbursement_view_page import EmployeeReimbursementViewPage
from selenium_content.poms.manager_reimbursement_view_page import ManagerReimbursementViewPage
from selenium_content.poms.reimbursement_request_page import ReimbursementRequestPage


import time

def before_all(context):
    context.driver = webdriver.Chrome()
    context.lp = LoginPage(context.driver)
    context.ep = EmployeePage(context.driver)
    context.mp = ManagerPage(context.driver)
    context.ervp = EmployeeReimbursementViewPage(context.driver)
    context.mrvp = ManagerReimbursementViewPage(context.driver)
    context.rrp = ReimbursementRequestPage(context.driver)

def before_step(context, step):
    time.sleep(1)

def after_all(context):
    # Remember to close the browser
    time.sleep(5)
    context.driver.quit()