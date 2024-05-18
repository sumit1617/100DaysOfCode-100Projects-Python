from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


EMAIL = "rahatsingh1817@gmail.com"
PASSWORD = "rahat@1806"

chrome_driver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")
sleep(2)

login = driver.find_element(By.XPATH, "//*[@id='o-654199900']/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a/span")
login.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, "//*[@id='o1912386320']/div/div/div[1]/div/div/div[3]/span/div[2]/button/span[2]")
fb_login.click()

#Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

fb_mail = driver.find_element(By.XPATH, "//*[@id='email']")
fb_password = driver.find_element(By.XPATH, "//*[@id='pass']")
fb_mail.send_keys(EMAIL)
fb_password.send_keys(PASSWORD)
fb_password.send_keys(Keys.ENTER)

#Switch back to Tinder window
driver.switch_to.window(base_window)
print(driver.title)