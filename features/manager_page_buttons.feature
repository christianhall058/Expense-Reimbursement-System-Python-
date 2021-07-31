Feature: Manager Page Buttons
    Background: An manager is on the manager page
      Given a user entered the correct credentials for a manager
      And the user clicked the login button

    Scenario: A manager is on the manager page and would like to click the Statistics button
      When a manager clicks the Statistics button
      Then the manager goes to the statistics page

    Scenario: A manager is on the manager page and would like to click the View reimbursement requests button
      When a manager clicks the View reimbursement requests button
      Then the manager goes to the View reimbursement requests page