
  Feature: Login
    Background: A user is on the home page
      Given a user is on the home page

    Scenario: An employee is on the home page and would like to login with correct credentials.
      When an employee enters the correct username and the correct password
      And the user clicked the login button
      Then the employee goes to the employee page

    Scenario: A manager is on the home page and would like to login with correct credentials.
      When a manager enters the correct username and the correct password
      And the user clicked the login button
      Then the manager goes to the manager page
