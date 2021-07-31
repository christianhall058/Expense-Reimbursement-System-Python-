from behave import *

@given('a user is on the home page')
def test_on_home_page(context):
    context.driver.get('http://127.0.0.1:5000/login')

@when('an employee enters the correct username and the correct password')
def test_employee_enters_username(context):
    context.lp.enter_employee_credentials()

@when('the user clicked the login button')
def test_employee_clicks_submit(context):
    context.lp.click_login_button()

@then('the employee goes to the employee page')
def test_employee_goes_to_employee_page(context):
    assert 'employee' in context.driver.current_url

@when('a manager enters the correct username and the correct password')
def test_manager_enters_username(context):
    context.lp.enter_manager_credentials()

@then('the manager goes to the manager page')
def test_manager_goes_to_manager_page(context):
    assert 'manager' in context.driver.current_url
