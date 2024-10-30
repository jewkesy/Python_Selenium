import pytest
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
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
PRODUCT_DESC = "Sauce Labs Fleece Jacket"

options = Options()
options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)
driver.get(URL) 

def enterText(element, value):
    element.clear();
    element.send_keys(value);

def test_title_and_logo():
    assert driver.current_url == URL+"/"

    appTitle = "Swag Labs"
    assert driver.title == appTitle
    logo = driver.find_element(By.CLASS_NAME, "login_logo")
    assert logo.text == appTitle

def test_login():
    assert driver.current_url == URL+"/"

    username = driver.find_element(By.ID, "user-name")
    password = driver.find_element(By.XPATH, '//*[@id="password"]')
    btnLogin = driver.find_element(By.NAME, "login-button")
    enterText(username, USERNAME_STD)
    enterText(password, PASSWORD_STD)
    btnLogin.click()
    assert driver.current_url == URL+"/inventory.html"


def test_inventory_page():
    assert driver.current_url == URL+"/inventory.html"

    xpath_firstItem = '//*[@id="inventory_container"]/div/div[1]/div[2]/div[2]/div'

    defaultSortPrice = driver.find_element(By.XPATH, xpath_firstItem).text
    assert defaultSortPrice == "$29.99"

    selectFilter = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
    selectFilter.select_by_value("hilo")

    HighLowSortPrice = driver.find_element(By.XPATH, xpath_firstItem).text
    assert HighLowSortPrice == "$49.99"

    xpath_jacketDesc = '//*[@id="item_5_title_link"]/div'

    itemDesc = driver.find_element(By.XPATH, xpath_jacketDesc)
    assert itemDesc.text == PRODUCT_DESC

    itemDesc.click()
    assert driver.current_url == URL+"/inventory-item.html?id=5"


def test_add_to_cart():
    assert driver.current_url == URL+"/inventory-item.html?id=5"

    xpath_cartBadge = '#shopping_cart_container > a > span'
    # check badge is not shown 
    badge = driver.find_elements(By.CSS_SELECTOR, xpath_cartBadge)
    assert len(badge) == 0

    btnAdd = driver.find_element(By.ID, 'add-to-cart')
    btnAdd.click()

    badge = driver.find_element(By.CSS_SELECTOR, xpath_cartBadge)

    assert badge.text == '1'
    badge.click()
    assert driver.current_url == URL+"/cart.html"


def test_purchase_item():
    assert driver.current_url == URL+"/cart.html"

    xpath_jacketDesc = '//*[@id="item_5_title_link"]/div'

    itemDesc = driver.find_element(By.XPATH, xpath_jacketDesc)
    assert itemDesc.text == PRODUCT_DESC

    btnCheckout = driver.find_element(By.ID, 'checkout')
    btnCheckout.click()
    assert driver.current_url == URL+"/checkout-step-one.html"


def test_checkout():
    assert driver.current_url == URL+"/checkout-step-one.html"

    firstName = driver.find_element(By.NAME, 'firstName')
    lastName = driver.find_element(By.ID, 'last-name')
    postalCode = driver.find_element(By.NAME, 'postalCode')

    enterText(firstName, 'Daryl')
    enterText(lastName, 'Jewkes')
    enterText(postalCode, 'AB12 3YZ')

    btnContinue = driver.find_element(By.NAME, 'continue')
    btnContinue.click()
    assert driver.current_url == URL+"/checkout-step-two.html"


def test_confirm_purchase():
    assert driver.current_url == URL+"/checkout-step-two.html"

    xpath_jacketDesc = '//*[@id="item_5_title_link"]/div'

    itemDesc = driver.find_element(By.XPATH, xpath_jacketDesc)
    assert itemDesc.text == PRODUCT_DESC

    btnContinue = driver.find_element(By.XPATH, '//*[@id="finish"]')
    btnContinue.click()
    assert driver.current_url == URL+"/checkout-complete.html"

def test_logout():
    burger = driver.find_element(By.ID, 'react-burger-menu-btn').click()

    xpath_logout = '//*[@id="logout_sidebar_link"]'

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, xpath_logout)))

    logout = driver.find_element(By.XPATH, xpath_logout)
    logout.click();

    assert driver.current_url == URL+"/"


def test_99_shutdown():
    driver.close()
