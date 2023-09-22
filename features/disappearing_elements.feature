# Created by given at 2022/08/26
Feature: Disappearing Page
  # Enter feature description here

  Scenario: Verify disappearing title and home, about, contact us and portfolio headings
    # Enter steps here
    Given the user open Disappearing elements page
    When the user click on home the page will go back to home page
    Then the user click on Disappearing Elements link the page will open again