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
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class AddRemovePageObjects(PageObject):

    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.add = None
        self.delete = None
        self.element = None

    def open(self):
        self.driver.get('{}/add_remove_elements/'.format(self.config.get('Test', 'url')))
        return self

    def click_add_element(self):
        self.add = self.driver.find_element_by_xpath('/html/body/div[2]/div/div/button')
        return self

    def click_delete_element(self):
        self.delete = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/div/button")
        self.delete.click()
        return self
