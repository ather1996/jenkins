from fileinput import close

from behave import *
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


@given('launch the chrome browser')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.driver.maximize_window()


@when('open the login page')
def step_impl(context):
    context.driver.get('https://practicetestautomation.com/practice-test-login/')
    context.driver.implicitly_wait(10)


@then('the user enters valid credentials')
def step_impl(context):
    context.driver.find_element(By.ID, "username").send_keys('student')
    context.driver.find_element(By.ID, "password").send_keys('Password123')
    context.driver.find_element(By.ID, "submit").click()
    time.sleep(6)  # Reduce for stability


@then('clicks on logout')
def step_impl(context):
    context.driver.find_element(By.XPATH, '//*[@id="loop-container"]/div/article/div[2]/div/div/div/a').click()
    time.sleep(40)
    context.driver.quit()


