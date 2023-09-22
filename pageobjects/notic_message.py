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
from pageobjects.message import MessagePageObject
from pageobjects.secure_area import SecureAreaPageObject


class NotificationMessagePageObject(PageObject):
    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.here = None

    def open(self):
        self.driver.get('{}/notification_message_rendered'.format(self.config.get('Test', 'url')))
        return self

    def here_note(self):
        self.here = self.driver.find_element(By.XPATH, "/html/body/div[2]/div/div/p/a")
        self.here.click()
        return self
