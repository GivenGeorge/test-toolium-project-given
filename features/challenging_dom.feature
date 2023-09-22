# Created by given at 2022/09/08
Feature: Challenging DOM Page
  # Enter feature description here

  Scenario: The user open the Challenging DOM page clicks on elements and get different outcome
    # Enter steps here
      Given The user open challenging dom page
        When the user test button
        When the user test button alert
        When the user test button success
        Then the user click edit option
        Then the user click delete option