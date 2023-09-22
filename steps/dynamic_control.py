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

from pageobjects.dynamic_control import DynamicControlPageObject


@given('the user open dynamic controls page')
def step_impl(context):
    context.current_page = DynamicControlPageObject()
    context.current_page.open()
    time.sleep(3)


@when('click the the checkbox , the clicks remove and the clicks enable')
def step_impl(context):
    context.current_page.test_remove()
    time.sleep(3)


@when('the user clicks add button')
def step_impl(context):
    context.current_page.test_add()
    time.sleep(3)


@when('the user clicks enable button')
def step_impl(context):
    context.current_page.test_enable()
    time.sleep(3)
