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
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ContextMenuPageObject(PageObject):

    def __init__(self, driver_wrapper=None, wait=5):
        super().__init__(driver_wrapper, wait)
        self.context_menu = None
        self.alertField = None

    def open(self):
        self.driver.get('{}/context_menu'.format(self.config.get('Test', 'url')))

    def click_context_menu(self, el: PageElement):
        action = ActionChains(self.driver)
        self.context_menu = self.driver.find_element_by_id("hot-spot")
        action.move_to_element(self.context_menu).perform()
        action.context_click(self.context_menu).perform()
        time.sleep(4)
        alert = self.driver.switch_to.alert
        alert.accept()
        return self
