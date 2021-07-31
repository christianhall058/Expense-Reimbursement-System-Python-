import time

from behave import *

@given('a manager clicks the View reimbursement requests button on the manager page')
def test_manager_clicks_view_reimbursements(context):
    context.mp.click_view_manager_requests()

@When('a manager clicks the approval button')
def test_manager_clicks_approve(context):
    context.mrvp.enter_manager_response()
    context.mrvp.click_approve()

@When('the manager reloads the page')
def test_manager_reload(context):
    context.driver.back()
    context.mp.click_view_manager_requests()

@Then('check the status to see if it is approved')
def test_manager_check_if_approved(context):
    assert 'true' in context.mrvp.check_status()