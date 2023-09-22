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
from selenium.common.exceptions import NoSuchElementException
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements.page_element import PageElement
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC


class BasicAuthPageObject(PageObject):
    def ini_page_elements(self):
        self.basic_auth = (By.XPATH, "//*[@id= 'content']//p")
        self.congratulations_text = (By.XPATH, "//*[@class='example']")

    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.congratulations_text = None
        self.basic_auth = None
        self.actual_text = None

    def open(self):
        self.driver.get('{}/basic_auth'.format(self.config.get('Test', 'url')))
        return self

    def send_correct_keys(self):
        actions = ActionChains(self.driver)
        actions.send_keys("admin").perform()
        actions.send_keys(Keys.TAB).perform()
        actions.send_keys("admin").perform()
        actions.send_keys(Keys.ENTER).perform()
        return self

