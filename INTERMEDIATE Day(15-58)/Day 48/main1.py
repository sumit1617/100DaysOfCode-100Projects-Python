from selenium import webdriver
from selenium.webdriver.common.by import By

chrome_driver_path = "D:\Development\chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("https://www.amazon.in/OnePlus-Emerald-Forest-128GB-Storage/dp/B09V2RSWBW/ref=sr_1_5?crid=1Y2R8J6BAUQMP&keywords=Oneplus%2Bphones&qid=1654930428&sprefix=oneplus%2Bphones%2Caps%2C1687&sr=8-5&th=1")
price = driver.find_elements(By.CLASS_NAME, ".a-span12 .a-offscreen")
print(price)


driver.quit()