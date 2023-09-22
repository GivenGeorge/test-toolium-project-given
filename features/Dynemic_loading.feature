# Created by given at 2022/09/06
Feature: Dynamic Loading Page
  # Enter feature description here

  Scenario: Dynamic loading page successfully open
    # Enter steps here
      Given The user open dynamic loading page
        When  the user clicks element1
        When the user click start button
        Then the text "hello world" will appear