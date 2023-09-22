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

from behave import given, when, then

from pageobjects.dropdown import DropDownPageObject


@given('the page "Dropdown" is open')
def step_impl(context):
    context.current_page = DropDownPageObject()
    context.current_page.open()
    time.sleep(1.5)


@when('Click dropdown box')
def step_impl(context):
    context.current_page = context.current_page.click_dropdown()
    time.sleep(1.5)


@then('Please select first option')
def step_impl(context):
    context.current_page.choose_dropdown1()
    time.sleep(1.5)
    context.current_page.choose_dropdown2()
    time.sleep(1.5)

