import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


CHROME_DRIVER_PATH = "D:\Development\chromedriver.exe"
SIMILAR_ACCOUNT = "virat.kohli"
USERNAME = "sumit.singh_18"
PASSWORD = "1817@sumit"


class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(5)
        username = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")
        username.send_keys(USERNAME)
        time.sleep(2)
        password = self.driver.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")
        password.send_keys(PASSWORD)
        time.sleep(2)
        password.send_keys(Keys.ENTER)
        time.sleep(10)
        close_popup = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        close_popup.click()
        time.sleep(10)


    def follow(self):
        self.driver.get("https://www.instagram.com/direct/t/340282366841710300949128237961995982126")
        time.sleep(15)
        follow = self.driver.find_element(By.XPATH, '//*[@id="mount_0_0_NW"]/div/div[1]/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div/div/div/div[3]/button[2]')
        follow.click()


    def send_message(self):
        pass


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.follow()
bot.send_message()