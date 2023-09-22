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


class JavaAlertsPageObject(PageObject):

    def __init__(self, driver_wrapper=None, wait=5):
        super().__init__(driver_wrapper, wait)
        self.click_prompt_alert = None
        self.click_confirm_alert = None
        self.click_simple_alert = None

    def open(self):
        self.driver.get('{}/javascript_alerts'.format(self.config.get('Test', 'url')))

    def simple_alert(self):
        action = ActionChains(self.driver)
        self.click_simple_alert = self.driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS Alert']")
        action.click(self.click_simple_alert).perform()
        time.sleep(3)
        alert = self.driver.switch_to.alert
        alert.accept()
        return self

    def confirm_alert(self):
        self.click_confirm_alert = self.driver.find_element(By.XPATH, "//button[normalize-space()='Click for JS "
                                                                      "Confirm']")
        actions = ActionChains(self.driver)
        actions.click(self.click_confirm_alert).perform()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.dismiss()
        return self

    def prompt_alert(self):
        self.click_prompt_alert = self.driver.find_element(By.XPATH,
                                                           "//button[normalize-space()='Click for JS Prompt']")
        actions = ActionChains(self.driver)
        actions.click(self.click_prompt_alert).perform()
        time.sleep(2)
        alert = self.driver.switch_to.alert
        alert.send_keys("Kinetic Skunk")
        alert.accept()
        return self
