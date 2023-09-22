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


class StatusCodePageObject(PageObject):

    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.status_500 = None
        self.status_404 = None
        self.status_301 = None
        self.click_here = None
        self.status_200 = None

    def open(self):
        self.driver.get('{}/status_codes'.format(self.config.get('Test', 'url')))
        return self

    def click_status_code_200(self):
        actions = ActionChains(self.driver)
        self.status_200 = self.driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[1]/a")
        actions.click(self.status_200).perform()
        time.sleep(3)
        actions = ActionChains(self.driver)
        self.click_here = self.driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
        actions.click(self.click_here).perform()
        return self

    def click_status_code_301(self):
        actions = ActionChains(self.driver)
        self.status_301 = self.driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[2]/a")
        actions.click(self.status_301).perform()
        time.sleep(4)
        actions = ActionChains(self.driver)
        self.click_here = self.driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
        actions.click(self.click_here).perform()
        return self

    def click_status_code_404(self):
        actions = ActionChains(self.driver)
        self.status_404 = self.driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[3]/a")
        actions.click(self.status_404).perform()
        time.sleep(2)
        actions = ActionChains(self.driver)
        self.click_here = self.driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
        actions.click(self.click_here).perform()
        return self

    def click_status_code_500(self):
        actions = ActionChains(self.driver)
        self.status_500 = self.driver.find_element(By.XPATH, "//*[@id='content']/div/ul/li[4]/a")
        actions.click(self.status_500).perform()
        time.sleep(3.5)
        actions = ActionChains(self.driver)
        self.click_here = self.driver.find_element(By.XPATH, "//*[@id='content']/div/p/a")
        actions.click(self.click_here).perform()
        return self


