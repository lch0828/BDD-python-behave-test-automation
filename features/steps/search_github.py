from behave import *
from selenium.webdriver.common.keys import Keys
import time
import os


@when('get google.com')
def step_impl(context):
    context.selenium_func.open('https://www.google.com/')

@when('enter keyword')
def step_impl(context):
    search = context.selenium_func.find_by_class('gLFyf gsfi')
    search.send_keys('github') 

@when('search')
def step_impl(context):
    search = context.selenium_func.find_by_class('gLFyf gsfi')
    search.send_keys('Keys.ENTER') 