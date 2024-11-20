import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.relative_locator import locate_with

    # Set of supported locator strategies.

    # ID = 'id'
    # XPATH = 'xpath'
    # LINK_TEXT = 'link text'
    # PARTIAL_LINK_TEXT = 'partial link text'
    # NAME = 'name'
    # TAG_NAME = 'tag name'
    # CLASS_NAME = 'class name'
    # CSS_SELECTOR = 'css selector'¶

URL = "https://www.saucedemo.com"

USERNAME_STD = "standard_user"
PASSWORD_STD = "secret_sauce"

options = Options()
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get(URL) 

def enterText(element, value):
    element.clear();
    element.send_keys(value);


def test_friendly_login():
    assert URL in driver.current_url

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.XPATH, '//*[@id="password"]')

    friendlyUsername = driver.find_element(locate_with(By.TAG_NAME, "input").above(password))
    friendlyPassword = driver.find_element(locate_with(By.TAG_NAME, "input").below(username))

    enterText(friendlyUsername, USERNAME_STD)
    enterText(friendlyPassword, PASSWORD_STD)

    friendlyLogin = driver.find_element(locate_with(By.ID, "login-button").near(friendlyPassword, 100))
    friendlyLogin.click()

    assert driver.current_url == URL+"/inventory.html"


def test_shutdown():
    assert URL in driver.current_url

    driver.quit()
