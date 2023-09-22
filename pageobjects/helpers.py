# -*- coding: utf-8 -*-
u"""
Copyright 2015 Telefónica Investigación y Desarrollo, S.A.U.
This file is part of Toolium.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject


class Helpers(PageObject):
    context_menu = None
    text_hello = None
    element1 = None
    close_button = None
    restart_ad = None
    file_upload = None
    file_submit = None
    status_200 = None
    click_here = None
    first_link = None
    second_link = None
    third_link = None
    click_map = None

    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.click_map = None
        self.third_link = None
        self.second_link = None
        self.first_link = None
        self.file_submit = None
        self.file_upload = None
        self.restart_ad = None
        self.close_button = None
        self.text_hello = None
        self.alert_message = None
        self.context_menu = None
        self.close_button = None

    def init_page_elements(self):
        self.context_menu = self.driver.find_elements(By.XPATH, "//*[@id='hot-spot']")
        self.alert_message = self.driver.find_elements(By.XPATH, "//*[@id='result']")
        self.text_hello = self.driver.find_elements(By.XPATH, "//h4[normalize-space()='Hello World!']")
        self.close_button = self.driver.find_elements(By.XPATH, "//*[@id='modal']/div[2]/div[3]/p")
        self.restart_ad = self.driver.find_elements(By.XPATH, "//*[@id='restart-ad']")
        self.file_upload = self.driver.find_elements(By.XPATH, "//*[@id='file-upload']")
        self.file_submit = self.driver.find_elements(By.XPATH, "//*[@id='file-submit']")
        self.first_link = self.driver.find_element(By.XPATH, "//*[@id='content']/div/a[1]")
        self.second_link = self.driver.find_element(By.XPATH, "//*[@id='content']/div/a[2]")
        self.third_link = self.driver.find_element(By.XPATH, "//*[@id='content']/div/a[3]")
        self.click_map = self.driver.find_element(By.XPATH, "//*[@id='map-link']/a")

