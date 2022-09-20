import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.in/OnePlus-Emerald-Forest-128GB-Storage/dp/B09V2RSWBW/ref=sr_1_5?crid=1Y2R8J6BAUQMP&keywords=Oneplus%2Bphones&qid=1654930428&sprefix=oneplus%2Bphones%2Caps%2C1687&sr=8-5&th=1"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,mr;q=0.8,hi;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(id="priceblock_ourprice").get_text()
price_without_currency = price.split("$")[1]
price_as_float = float(price_without_currency)
print(price_as_float)