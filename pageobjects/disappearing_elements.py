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
from xmlrpc.client import boolean

from selenium.webdriver.common.by import By
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class DisappearingElements(PageObject):
    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.link = None
        self.home_button = None

    def open(self):
        self.driver.get('{}/disappearing_elements'.format(self.config.get('Test', 'url')))
        return self

    def click_home_button(self):
        self.home_button = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/ul/li[1]/a')
        self.home_button.click()
        time.sleep(1)
        return self

    def click_link(self):
        self.link = self.driver.find_element(By.XPATH, '//*[@id="content"]/ul/li[9]/a')
        self.link.click()
        self.driver.refresh()
        time.sleep(1.5)
        