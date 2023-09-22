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
from toolium.pageelements.page_element import PageElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class DynamicLoadingPageObject(PageObject):

    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.button_create = None
        self.button_start = None
        self.text_hello = None
        self.element_1 = None

    def open(self):
        self.driver.get('{}/dynamic_loading'.format(self.config.get('Test', 'url')))

    def click_element(self):
        actions = ActionChains(self.driver)
        self.element_1 = self.driver.find_element(By.XPATH, "//*[@id='content']/div/a[1]")
        actions.click(self.element_1).perform()
        time.sleep(2)
        return self

    def click_start(self):
        actions = ActionChains(self.driver)
        self.button_start = self.driver.find_element(By.XPATH, "//button[normalize-space()='Start']")
        actions.click(self.button_start).perform()
        time.sleep(3)
        return self


