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

from needle import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.wait import WebDriverWait
chrome_options = Options()
chrome_options.add_experimental_option("detach", True)
from toolium.pageobjects.page_object import PageObject
from toolium.pageelements import *


class DropDownPageObject(PageObject):
    def __init__(self, driver_wrapper=None, wait=False):
        super().__init__(driver_wrapper, wait)
        self.option2 = None
        self.option1 = None
        self.dropdown_box = None

    def open(self):
        self.driver.get('{}/dropdown'.format(self.config.get('Test', 'url')))
        return self

    def click_dropdown(self):
        self.dropdown_box = Button(By.XPATH, "//*[@id='dropdown']")
        self.dropdown_box.click()
        return self

    def choose_dropdown1(self):
        self.option1 = Button(By.XPATH, "/html/body/div[2]/div/div/select/option[2]")
        self.option1.click()
        return self

    def choose_dropdown2(self):
        self.option2 = Button(By.XPATH, "/html/body/div[2]/div/div/select/option[3]")
        self.option2.click()
        return self
