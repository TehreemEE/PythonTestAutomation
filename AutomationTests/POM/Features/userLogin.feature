# Feature file to implement behave for user login to Equitime

Feature: Equitime User Login

# This scenario will check the login with one valid credentials only
# Scenario will execute only one round of test
  Scenario: Login to Equitime Application with one valid credentials
    Given user launch firefox browser
    When user open equitime homepage and click login button
    #only one parameters for email and password is used here
    And Enter email "evita.abishag@last-shipment.com" and password "ypgb62T9pMmPuFHd"
    And Submits the form
    Then User must successfully login to dashboard and Company Dashboard, including all related company contracts, is available
    Then click logout button
    Then close browser

# This is the scenario outline to implement the data driven testing for checking multiple user login
# To pass multiple parameters to the steps Scenario Outline is implemented
# Based on the Examples scenario outline will implement multiple times
  Scenario Outline: Login to Equitime Application with multiple credentials
    Given user launch firefox browser
    When user open equitime homepage and click login button
# This step will use the data defined in Examples
    And Enter email "<username>" and password "<password>"
    And Submits the form
    Then User must successfully login to dashboard and Company Dashboard, including all related company contracts, is available
    Then click logout button
    Then close browser

# This scenario outline will execute 14 times
# Example is a Gherkin keyword
# Username and password are the headers, underneath them is the data that will be executed
    Examples:
      | username                           | password         |
      | alte.vsevolod@last-shipment.com    | eCtW7ZVkMKPmRy7F |
      | neptunus.chelsey@dshipment.com     | rmeMD3M3YFNXJ5HL |
      | bertina.figaro@dshipment.com       | hgL6mcNDR2rYkaQp |
      | avrora.herman@smugglee.com         | NKNTSjY3HLhfdRpM |
      | amalija.patrizio@smugglee.com      | 77aPWK2sd665hXwP |
      | abc@abc.com                        | 123456           |
      | sahar.milenko@luggagex.com         | X22KqZeQyU5AyNRr |
      | phyllida.drest@luggagex.com        | HD3sdhY97PLfhRUr |
      | delfina.hila@constructsy.com       | bjp9V3Sc9g2Xcnwc |
      | elifalet.kunigunde@constructsy.com | k6cQNtXv8BCaDxaw |
      | elifalet.kunigunde@constructsy.com | 123456           |
      | sahar@luggagex.com                 | X22KqZeQyU5AyNRr |
      | elfina.dejong@construct.com        | 7ZUFQx8y8Yuhuxwp |
      | lifaleth.dejong@construct.com      | EPbU4tgvxPjTZT8d |