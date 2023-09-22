# Created by given at 2022/09/07
Feature: The File Upload Page Open
  # Enter feature description here

  Scenario: The user choose a file and upload the file
    # Enter steps here
    Given The user open file-upload page
    When  the user clicks on "choose-file"
    When the user choose a file and select enter
    Then the user clicks on "upload" the .txt file will upload