Feature: Login functionality

  Scenario: Successful login
    Given launch the chrome browser
    When open the login page
    Then the user enters valid credentials
    Then clicks on logout
