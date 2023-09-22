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
from pageobjects.basic_auth import BasicAuthPageObject


@given('The user open basic auth page')
def step_impl(context):
    context.current_page = BasicAuthPageObject()
    context.current_page.open()
    time.sleep(5)


@then('the user fill login form')
def step_impl(context):
    context.current_page.send_correct_keys()
    time.sleep(5)


