# Created by given at 2022/09/08
Feature: The JavaScript Alerts
  # Enter feature description here

  Scenario: The user successfully open JavaScript Alerts page and handle the three alerts
    # Enter steps here
    Given The user open javaScript alerts
      When the user clicks on simple alert and it will auto accept alert
      When the user click on confirm alert user clicks cancel to dismiss alert
      When the user click on prompt alert and type keys in