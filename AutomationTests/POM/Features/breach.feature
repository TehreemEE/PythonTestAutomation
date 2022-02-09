# Feature file to implement behave for raisning breach flow in Equitime application

Feature: Equitime Raise Breach

# This scenario will check the login with one valid credentials only
# Scenario will execute only one round of test
  Scenario: Raise Breach in Equitime Application
    Given user launch browser
    When User click login button on equitime homepage
    And Enter valid credentials email "evita.abishag@last-shipment.com" and password "ypgb62T9pMmPuFHd"
    And Submits the login form
    Then User should be logged in Company Dashboard, and all related company contracts, is available
    When User selects the last contract in the list by clicking contract view button on dashboard page
    Then contract details open
    And User fills in a Breach Description and submits the breach form
    Then the same Contract View is displayed
    And the created breach is present
    Then close the browser

