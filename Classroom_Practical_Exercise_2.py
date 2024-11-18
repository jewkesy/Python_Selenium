import pytest
import time

# Send Keys Example
# Opens a python webpage, searches for 'python'

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

URL = "https://www.python.org/";
q = "python"
# f = open("data.txt").read()
# q = f

donateURL = "https://psfmember.org/civicrm/contribute/transact/?reset=1&id=2"

def test_using_locators():
	driver.get(URL)
	assert driver.current_url == URL

	# Donate button
	byClassname = driver.find_element(By.CLASS_NAME, "donate-button")
	byClassname.click()
	assert driver.current_url == donateURL

	driver.get(URL)
	byLinkText = driver.find_element(By.LINK_TEXT, "Donate")
	byLinkText.click()
	assert driver.current_url == donateURL

	driver.get(URL)
	byPartialLinkText = driver.find_element(By.PARTIAL_LINK_TEXT, "onat")
	byPartialLinkText.click()
	assert driver.current_url == donateURL

	# driver.get(URL)
	# byTagName = driver.find_element(By.TAG_NAME, "a")

	# assert driver.current_url == donateURL


	driver.get(URL)
	byId = driver.find_element(By.ID, "id-search-field")
	byId.send_keys("byID")

	byClass = driver.find_element(By.CLASS_NAME, "search-field")
	byClass.send_keys("byClass")

	byName = driver.find_element(By.NAME, "q")
	byName.send_keys("byName")

	# byTagname = driver.find_elements(By.TAG_NAME, "input")[0]
	# byTagName.send_keys("byTag")

	submitBtn = driver.find_element(By.NAME, "submit").click()

	assert driver.current_url == URL + "search/?q=byIDbyClassbyName&submit="

	# time.sleep(2)

	driver.quit()
