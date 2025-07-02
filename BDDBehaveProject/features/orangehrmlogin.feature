Feature: OrangeHRM Login
   
    Scenario: Login to OrangeHRM with valid parameters
    Given I launch chrome browser 
    When I open OrangeHRM Homepage
    And Enter username "admin" and password "admin123"
    And Click on login button
    Then User must successfully login to the Dashboard page
    