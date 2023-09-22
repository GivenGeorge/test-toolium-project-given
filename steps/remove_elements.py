import time
from behave import given, when, then
from pageobjects.helpers import Helpers
from pageobjects.remove_elements import AddRemovePageObjects


@given('the user open add/remove page')
def step_impl(context):
    context.current_page = AddRemovePageObjects()
    context.current_page.open()
    time.sleep(2)


@when('the user clicks on the add element button')
def step_impl(context):
    context.current_page.click_add_element()
    time.sleep(3)


@then('the user clicks on remove button and element will be remove')
def step_impl(context):
    context.current_page.click_delete_element()
    time.sleep(3)
