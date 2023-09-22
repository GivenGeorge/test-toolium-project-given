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
from selenium.webdriver.chrome.options import Options
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from toolium.pageelements.page_element import PageElement
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ChallengingDomPageObject(PageObject):

    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.click_delete = None
        self.click_edit = None
        self.button_success = None
        self.button_alert = None
        self.click_button = None

    def open(self):
        self.driver.get('{}/challenging_dom'.format(self.config.get('Test', 'url')))
        return self

    def test_button(self):
        self.click_button = self.driver.find_element(By.XPATH, '//a[@class="button"]')
        self.click_button.click()
        time.sleep(2)
        return self

    def test_button_alert(self):
        self.button_alert = self.driver.find_element(By.XPATH, '//a[@class="button alert"]')
        self.button_alert.click()
        time.sleep(2.5)
        return self

    def test_button_success(self):
        self.button_success = self.driver.find_element(By.XPATH, '//a[@class="button alert"]')
        self.button_success.click()
        time.sleep(3.5)
        return self

    def click_edit_element(self):
        self.click_edit = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/table/tbody/tr['
                                                             '1]/td[7]/a[1]')
        self.click_edit.click()
        time.sleep(2)
        return self

    def click_delete_element(self):
        self.click_delete = self.driver.find_element(By.XPATH, '//*[@id="content"]/div/div/div/div[2]/table/tbody/tr['
                                                               '1]/td[7]/a[2]')
        self.click_delete.click()
        time.sleep(2)
        return self
