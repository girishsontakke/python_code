from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from secrets import pw


class insta_bot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome(
            executable_path='C:\webdrivers\chromedriver.exe')
        self.driver.get("https://www.instagram.com/")
        sleep(2)
        self.username = username
        self.driver.find_element_by_xpath("//input[@name = 'username']")\
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name = 'password']")\
            .send_keys(pw)
        self.driver.find_element_by_xpath("//button[@type='submit']")\
            .click()
        sleep(12)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]")\
            .click()
        sleep(4)

    def unfollower(self):
        self.driver.find_element_by_xpath("//a[@class = 'gmFkV']")\
            .click()
        sleep(3)
        self.driver.find_element_by_class_name("g47SY loXF2")\
            .click()


my_bot = insta_bot("girishsontakke", pw)
my_bot.unfollower()
