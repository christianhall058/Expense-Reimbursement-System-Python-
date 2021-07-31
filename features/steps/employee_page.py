from behave import *

@given('a user entered the correct credentials for a employee')
def test_employee_login_credentials(context):
    context.driver.get('http://127.0.0.1:5000/login')
    context.lp.enter_employee_credentials()

@given('the user clicked the login button')
def test_employee_clicks_login_btn(context):
    context.lp.click_login_button()

@when('an employee clicks the Request Reimbursement button')
def test_employee_clicks_request(context):
    context.ep.click_make_a_reimbursement_request()

@then('the emplyee goes to the make reimbursement request page')
def test_employee_goes_to_request_page(context):
    assert 'Rembursement Request' in context.driver.title

@when('an employee clicks the View past reimbursement requests button')
def test_employee_clicks_view_btn(context):
    context.ep.click_view_past_reimbursement_requests()

@then('the employee goes to the View past reimbursement requests page')
def test_employee_goes_to_view_page(context):
    assert 'Request View' in context.driver.title
