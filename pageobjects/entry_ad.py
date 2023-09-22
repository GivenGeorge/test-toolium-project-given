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
from selenium.common.exceptions import NoSuchElementException
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements.page_element import PageElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class EntryAdPageObject(PageObject):

    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.restart_ad = None
        self.close_button = None

    def open(self):
        self.driver.get('{}/entry_ad'.format(self.config.get('Test', 'url')))
        return self

    def click_close(self, el: PageElement):
        actions = ActionChains(self.driver)
        self.close_button = self.driver.find_element_by_id("modal")
        actions.move_to_element(self.close_button).perform()
        actions.click(self.close_button).perform()
        return self

    def click_restart_ad(self, el: PageElement):
        actions = ActionChains(self.driver)
        self.restart_ad = self.driver.find_element_by_id("restart-ad")
        actions.move_to_element(self.restart_ad).perform()
        actions.click(self.restart_ad).perform()
        self.driver.refresh()
        return self



