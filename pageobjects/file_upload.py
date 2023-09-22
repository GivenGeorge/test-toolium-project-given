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
from selenium.webdriver.common.keys import Keys


class FileUploadPageObject(PageObject):

    def __init__(self, driver_wrapper=None, wait=5):
        super().__init__(driver_wrapper, wait)
        self.file = None
        self.file_submit = None
        self.file_upload = None

    def open(self):
        self.driver.get('{}/upload'.format(self.config.get('Test', 'url')))

    def click_choose_file(self, el: PageElement):
        actions = ActionChains(self.driver)
        self.file_upload = self.driver.find_element_by_id("file-upload")
        actions.click(self.file_upload).perform()
        time.sleep(3)
        return self

    def choose_file(self):
        actions = ActionChains(self.driver)
        self.file = self.driver.find_element(By.ID, "fileUpload")
        self.driver.switch_to.active_element()
        self.file.send_keys("/home/given/Documents/some-file.txt")

        actions.send_keys(Keys.ENTER).perform()
        time.sleep(3)

    def click_submit_button(self, el: PageElement):
        actions = ActionChains(self.driver)
        self.file_submit = self.driver.find_element_by_id("file-submit")
        actions.move_to_element(self.file_submit).perform()
        actions.click(self.file_submit).perform()
        return self
