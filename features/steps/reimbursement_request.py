import time

from behave import *

@given('an employee clicks the Request Reimbursement button on the employee page')
def test_employee_clicks_request(context):
    context.ep.click_make_a_reimbursement_request()

@When('the employee enters amount and reason')
def test_employee_enters_a_and_r(context):
    context.rrp.enter_reason()
    context.rrp.enter_amount()

@When('the employee presses the submit button')
def test_employee_presses_submit(context):
    context.rrp.click_submit()

@Then('check the reimbursement view page to see if it went through')
def test_reimbursement_view(context):
    context.driver.back()
    context.ep.click_view_past_reimbursement_requests()
    time.sleep(3)
    assert 'true' in context.ervp.get_amount_reason_value()