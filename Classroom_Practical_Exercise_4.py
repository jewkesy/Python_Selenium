import pytest
import time

# Send Keys Example
# Opens a python webpage, searches for 'python' using CSS Selector

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

options = Options()
# options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

URL = "https://www.python.org/";
q = "python"

donateURL = "https://psfmember.org/civicrm/contribute/transact/?reset=1&id=2"

def test_can_use_css_selector():
	driver.get(URL)
	assert driver.current_url == URL

	searchBox = driver.find_element(By.CSS_SELECTOR, "#id-search-field").send_keys(q)
	submitBtn = driver.find_element(By.CSS_SELECTOR, "button#submit.search-button").click()

	assert driver.current_url == URL + "search/?q=" + q + "&submit="

	driver.get(URL)
	assert driver.current_url == URL

	donateBtn = driver.find_element(By.CSS_SELECTOR, "a.donate-button")
	donateBtn.click()
	assert driver.current_url == donateURL

	# time.sleep(2)

	driver.quit()
