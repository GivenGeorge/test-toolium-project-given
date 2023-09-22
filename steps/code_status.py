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
from pageobjects.helpers import Helpers
from pageobjects.code_status import StatusCodePageObject


@given('The user open status code page')
def step_impl(context):
    context.current_page = StatusCodePageObject()
    context.current_page.open()
    time.sleep(1)


@when('the user click on "200" and click ons "here"')
def step_impl(context):
    context.current_page.click_status_code_200()
    time.sleep(5)


@when('the user click on "301" and click ons "here"')
def step_impl(context):
    context.current_page.click_status_code_301()
    time.sleep(5)


@when('the user click on "404" and click ons "here"')
def step_impl(context):
    context.current_page.click_status_code_404()
    time.sleep(5)


@when('the user click on "500" and click ons "here"')
def step_impl(context):
    context.current_page.click_status_code_404()
    time.sleep(5)
