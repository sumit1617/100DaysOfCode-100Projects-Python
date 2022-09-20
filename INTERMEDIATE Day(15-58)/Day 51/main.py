from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

TWITTER_USERNAME = "sumitsingh____"
TWITTER_USERNAME2 = ""
TWITTER_PW = "sumit4734"
PROMISED_UP = 50
PROMISED_DOWN = 50
CHROME_DRIVER_PATH = "D:\Development\chromedriver.exe"

class InternetSpeedTwitterBot:

    def __init__(self):
        self.driver = webdriver.Chrome(CHROME_DRIVER_PATH)
        self.promised_up = PROMISED_UP
        self.promised_down = PROMISED_DOWN
        self.download_speed = 0
        self.upload_speed = 0


    def get_internet_speed(self):
        self.driver.get(url="https://www.speedtest.net")
        # consentbutton = self.driver.find_element(By.ID, "_evidon-banner-acceptbutton")
        gobutton = self.driver.find_element(By.CLASS_NAME, "start-button")
        # consentbutton.click()
        gobutton.click()
        time.sleep(90)
        self.download_speed = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span")
        self.download_speed = float(self.download_speed.text)
        self.upload_speed = self.driver.find_element(By.XPATH, "/html/body/div[3]/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span")
        self.upload_speed = float(self.upload_speed.text)

    def tweet_about_speed(self):
        self.driver.get(url="https://twitter.com/i/flow/login")
        # cookies = self.driver.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div/div/div/div/div/div[2]/div[1]/div/span/span")
        time.sleep(2)
        username_field = self.driver.find_element(By.NAME, 'text')
        username_field.send_keys(TWITTER_USERNAME)
        time.sleep(1)
        username_field.send_keys(Keys.ENTER)
        time.sleep(2)
        password_field = self.driver.find_element(By.NAME, "password")
        password_field.send_keys(TWITTER_PW)
        time.sleep(1)
        password_field.send_keys(Keys.ENTER)
        time.sleep(3)
        self.driver.get("https://twitter.com/compose/tweet")
        time.sleep(3)
        actions = ActionChains(self.driver)
        actions.send_keys(f"Internet speed at time of testing was download:{self.download_speed} Mbps, upload: {self.upload_speed} Mbps")
        actions.send_keys(Keys.ENTER)
        actions.perform()
        tweet_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]')
        tweet_button.click()


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_about_speed()
