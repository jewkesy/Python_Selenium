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

donateURL = "https://psfmember.org/civicrm/contribute/transact/?reset=1&id=2"
URL = "https://www.python.org/";
q = "python"

def test_send_keys():
	driver.get(URL)
	assert driver.current_url == URL

	# Donate button
	byXpath = driver.find_element(By.XPATH, '//*[@class="donate-button"]')
	byXpath.click()
	assert driver.current_url == donateURL

	driver.get(URL)
	assert driver.current_url == URL

	searchBox = driver.find_element(By.XPATH, '//*[@id="id-search-field"]').send_keys(q)
	submitBtn = driver.find_element(By.XPATH, '//*[@id="submit"]').click()

	assert driver.current_url == URL + "search/?q=" + q + "&submit="

	# time.sleep(2)

	driver.quit()


# use xpath to find search box, donate button, search submit