Feature: Reimbursement Request
    Background: An employee is on the reimbursement request page
      Given a user entered the correct credentials for a employee
      And the user clicked the login button
      And an employee clicks the Request Reimbursement button on the employee page


    Scenario: A employee is on the reimbursement request page and would like to Request a Reimbursement
      When the employee enters amount and reason
      And the employee presses the submit button
      Then check the reimbursement view page to see if it went through