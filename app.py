from selenium import webdriver
from selenium.webdriver.common import keys
import time


#Twitterbot Template Class
class TwitterBot:
    #constructor assigns login credentials and webdriver to self.
    def __init__(self,username,password):
        self.username = username
        self.password = password       
        self.bot = webdriver.Firefox()
    # Login with attributes attached to self
    def login(self):
        bot = self.bot
        bot.get('https://twitter.com/')
        time.sleep(5) # waits (#) seconds to allow site to load
        


