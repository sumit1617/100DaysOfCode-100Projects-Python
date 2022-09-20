from selenium import webdriver
from selenium.webdriver.common.by import By


chrome_driver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("http://secure-retreat-92358.herokuapp.com/")

f_name = driver.find_element(By.NAME, "fName")
f_name.send_keys("Sumit")

l_name = driver.find_element(By.NAME, "lName")
l_name.send_keys("Singh")

email = driver.find_element(By.NAME, "email")
email.send_keys("sumit1456@gmail.com")

sign_up = driver.find_element(By.CLASS_NAME, "btn")
sign_up.click()
