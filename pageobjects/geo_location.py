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


class GeoLocationsPageObject(PageObject):
        
    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.click_map = None
        self.whereami_button = None

    def open(self):
        self.driver.get('{}/geolocation'.format(self.config.get('Test', 'url')))
        return self

    def click_whereami_button(self, el: PageElement):
        action = ActionChains(self.driver)
        self.whereami_button = self.driver.find_element(By.XPATH, "//*[@id='content']/div/button")
        action.click(self.whereami_button).perform()
        time.sleep(2)

    def click_map_link(self, el: PageElement):
        actions = ActionChains(self.driver)
        self.click_map = self.driver.find_element_by_id('map-link')
        actions.click(self.click_map).perform()
        time.sleep(3)
