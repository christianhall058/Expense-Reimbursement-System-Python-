from behave import *

@given('a user entered the correct credentials for a manager')
def test_manager_login_credentials(context):
    context.driver.get('http://127.0.0.1:5000/login')
    context.lp.enter_manager_credentials()

@when('a manager clicks the Statistics button')
def test_manager_clicks_stat(context):
    context.mp.click_statistics()

@then('the manager goes to the statistics page')
def test_manager_goes_to_stat_page(context):
    assert 'Statistics' in context.driver.title

@when('a manager clicks the View reimbursement requests button')
def test_manager_clicks_view_btn(context):
    context.mp.click_view_manager_requests()

@then('the manager goes to the View reimbursement requests page')
def test_manager_goes_to_view_page(context):
    assert 'Manager Request View' in context.driver.title