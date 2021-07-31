Feature: Reimbursement Status Change
    Background: An manager is on the manager reimbursement view page
      Given a user entered the correct credentials for a manager
      And the user clicked the login button
      And a manager clicks the View reimbursement requests button on the manager page

    Scenario: A manager is on the reimbursement view page and would like to approve a request with response
      When a manager clicks the approval button
      And the manager reloads the page
      Then check the status to see if it is approved
