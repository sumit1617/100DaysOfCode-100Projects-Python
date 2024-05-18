from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

PROMISED_DOWN = 40
PROMISED_UP = 8
CHROME_DRIVER_PATH = "D:\Development\chromedriver.exe"
TWITTER_USERNAME = "sumitsingh____"
TWITTER_PASSWORD = "sumit4734"


class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        time.sleep(3)
        go_button = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div["
                                                       "3]/div[1]/a/span[4]")
        go_button.click()

        time.sleep(80)
        self.up = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div["
                                                     "3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text
        self.down = self.driver.find_element(By.XPATH, "//*[@id='container']/div/div[3]/div/div/div/div[2]/div["
                                                       "3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div["
                                                       "2]/span").text
        print(f"down = {self.down}")
        print(f"up = {self.up}")

    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")

        time.sleep(2)
        username = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")
        username.send_keys(TWITTER_USERNAME)
        time.sleep(2)
        username.send_keys(Keys.ENTER)
        password = self.driver.find_element(By.XPATH, "//*[@id='layers']/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")
        password.send_keys(TWITTER_PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(2)

        tweet = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div[2]/div/div/div/label/div[1]/div/div/div/div/div[2]/div/div/div/div")
        tweets = f"Hey Internet Provider, Why my Internet Speed is {self.down}down/{self.up}up When I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?🤔 "
        tweet.send_keys(tweets)
        time.sleep(5)

        tweet_button = self.driver.find_element(By.XPATH, "//*[@id='react-root']/div/div/div[2]/main/div/div/div/div/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[3]/div/div/div[2]/div[3]/div/span/span")
        tweet_button.click()
        time.sleep(5)
        self.driver.quit()


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()




