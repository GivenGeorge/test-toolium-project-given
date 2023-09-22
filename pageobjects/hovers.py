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


class HoverPageObject(PageObject):
    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.hover_img_three = None
        self.hover_img_two = None
        self.hover_img_one = None

    def open(self):
        self.driver.get('{}/hovers'.format(self.config.get('Test', 'url')))
        return self

    def hover_img1(self):
        actions = ActionChains(self.driver)
        self.hover_img_one = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/img')
        actions.move_to_element(self.hover_img_one).perform()
        time.sleep(3)
        return self

    def hover_img2(self):
        actions = ActionChains(self.driver)
        self.hover_img_two = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/img')
        actions.move_to_element(self.hover_img_two).perform()
        time.sleep(3)
        return self

    def hover_img3(self):
        actions = ActionChains(self.driver)
        self.hover_img_three = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div[3]/img')
        actions.move_to_element(self.hover_img_three).perform()
        time.sleep(3)
        return self

