from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

URL = "https://www.saucedemo.com"

USERNAME_STD = "standard_user"
PASSWORD_STD = "secret_sauce"

driver = webdriver.Chrome()

def test_login():
    driver.get(URL)
    assert driver.current_url == URL+"/"

    driver.find_element(By.ID, "user-name").send_keys(USERNAME_STD);
    driver.find_element(By.XPATH, '//input[@id="password"]').send_keys(PASSWORD_STD);
    driver.find_element(By.NAME, "login-button").click()
    
    assert driver.current_url == URL+"/inventory.html"
    assert driver.title == "Swag Labs"

    driver.close()
