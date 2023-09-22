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
from pageobjects.challenging_dom import ChallengingDomPageObject


@given('the user open Challenging Dom page')
def step_impl(context):
    context.current_page = ChallengingDomPageObject()
    context.current_page.open()
    time.sleep(2)


@when('the user test button')
def step_impl(context):
    context.current_page.test_button()
    time.sleep(3)


@when('the user test button alert')
def step_impl(context):
    context.current_page.test_button_alert()
    time.sleep(3)


@when('the user test button success')
def step_impl(context):
    context.current_page.test_button_success()
    time.sleep(3)


@then('the user click edit option')
def step_impl(context):
    context.current_page.click_edit_element()
    time.sleep(3)


@then('the user click delete option')
def step_impl(context):
    context.current_page.click_delete_element()
    time.sleep(3)
