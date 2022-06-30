from selenium import webdriver
from util.selenium_web import get_browser
 

def before_all(context):
    selenium_func = get_browser('chrome')
    context.selenium_func = selenium_func

def after_all(context):
    context.selenium_func.close()