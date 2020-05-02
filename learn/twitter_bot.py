from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import ui
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from time import sleep
from secrets import pw


class twitter_bot:
    def __init__(self):
        self.driver = webdriver.Chrome(
            executable_path='C:\webdrivers\chromedriver.exe')
        bot = self.driver
        bot.get("https://twitter.com/explore")
        sleep(3)
        bot.find_element_by_xpath("//*[contains(text(), 'Log in')]")\
            .click()
        sleep(3)

    def login(self, username, pw):
        bot = self.driver
        bot.find_element_by_xpath("//input[@name= 'session[username_or_email]']")\
            .send_keys(username)
        bot.find_element_by_xpath("//input[@name= 'session[password]']")\
            .send_keys(pw)
        sleep(3)
        bot.find_element_by_xpath("//input[@name= 'session[password]']")\
            .send_keys(Keys.RETURN)
        sleep(3)

    def follow(self, hashtag):
        bot=self.driver
        bot.get('https://twitter.com/search?q='+hashtag+'&src=typed_query')
        sleep(3)
        for i in range(1, 10):
          bot.execute_script('window.scrollTo(0,document.body.scrollHeight)')
          sleep(10)
          tweets=bot.find_elements_by_class_name('tweet')
          links = [elem.get_attribute('data-permalink-path')
                   for elem in tweets]
          print(links)
        
          


mybot = twitter_bot()
mybot.login('girishsontakke7@gmail.com', pw)
mybot.follow('webdevlopment')