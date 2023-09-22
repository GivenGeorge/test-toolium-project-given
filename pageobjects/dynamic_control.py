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
import time

from selenium.webdriver.common.by import By

from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *
from pageobjects.message import MessagePageObject


class DynamicControlPageObject(PageObject):
    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.click_enable = None
        self.click_add = None
        self.click_remove = None
        self.checkbox_example = None

    def init_page_elements(self):
        self.click_box = Button(By.XPATH, "//*[@id='checkbox']/input")
        self.add_button = Button(By.XPATH, "//form[@id='checkbox-example']/button")
        self.enable_button = Button(By.XPATH, "//form[@id='input-example']/button")
        self.message = MessagePageObject()

    def open(self):
        self.driver.get('{}/dynamic_controls'.format(self.config.get('Test', 'url')))
        return self

    def click_checkbox(self):
        self.checkbox_example = self.driver.find_element(By.XPATH, '//*[@id="checkbox"]/input')
        self.checkbox_example.click()
        time.sleep(1)
        return self

    def test_remove(self):
        self.click_remove = self.driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
        self.click_remove.click()
        time.sleep(1.5)
        return self

    def test_add(self):
        self.click_add = self.driver.find_element(By.XPATH, "//form[@id='checkbox-example']/button")
        self.click_add.click()
        time.sleep(2)
        return self

    def test_enable(self):
        self.click_enable = self.driver.find_element(By.XPATH, "//form[@id='input-example']/button")
        self.click_enable.click()
        time.sleep(2.5)
        return self
