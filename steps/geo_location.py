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
from pageobjects.geo_location import GeoLocationsPageObject


@given('the user open "Geolocation" page')
def step_impl(context):
    context.current_page = GeoLocationsPageObject()
    context.current_page.open()


@when('clicks on the "where am I" button')
def step_impl(context):
    context.current_page.click_whereami_button()
    time.sleep(2)


@when('the "latitude" and "longitude" will show')
def step_impl(context):
    context.current_page = GeoLocationsPageObject()
    time.sleep(4)


@when('clicks on the "see it on google" link')
def step_impl(context):
    context.current_page.click_map_link(Helpers.click_map)
    time.sleep(4)
