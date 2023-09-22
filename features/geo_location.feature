# Created by given at 2022/08/30
Feature: Geolocation page
  # Enter feature description here

  Scenario: Geolocation page is successfully open
    # Enter steps here
    Given The user open "Geolocation" page
      When clicks on the "where am I" button
       When the "latitude" and "longitude" will show
        When clicks on the "see it on google" link