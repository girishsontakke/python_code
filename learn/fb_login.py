from selenium import webdriver
from time import sleep
from secrets import pw
browser = webdriver.Chrome()
browser.get("http://www.facebook.com")
username = browser.find_element_by_id("email")
password = browser.find_element_by_id("pass")
submit = browser.find_element_by_id("loginbutton")
username.send_keys("girishsontakke7@gmail.com")
password.send_keys(pw)
submit.click()