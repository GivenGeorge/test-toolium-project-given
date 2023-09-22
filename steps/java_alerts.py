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
from pageobjects.java_alerts import JavaAlertsPageObject


@given('The user open javaScript alerts')
def step_impl(context):
    context.current_page = JavaAlertsPageObject()
    context.current_page.open()
    time.sleep(3)


@when('the user clicks on simple alert and it will auto accept alert')
def step_impl(context):
    context.current_page.simple_alert()
    time.sleep(3)


@when('the user click on confirm alert user clicks cancel to dismiss alert')
def step_impl(context):
    context.current_page.confirm_alert()
    time.sleep(3)


@when('the user click on prompt alert and type keys in')
def step_impl(context):
    context.current_page.prompt_alert()
    time.sleep(3)
