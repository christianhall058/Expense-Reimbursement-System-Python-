Feature: Employee Page Buttons
    Background: An employee is on the employee page
      Given a user entered the correct credentials for a employee
      And the user clicked the login button

    Scenario: A employee is on the employee page and would like to click the Request Reimbursement button
      When an employee clicks the Request Reimbursement button
      Then the emplyee goes to the make reimbursement request page

    Scenario: A employee is on the employee page and would like to click the View past reimbursement requests button
      When an employee clicks the View past reimbursement requests button
      Then the employee goes to the View past reimbursement requests page