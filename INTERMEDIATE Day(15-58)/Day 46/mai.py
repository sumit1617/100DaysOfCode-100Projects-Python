from bs4 import BeautifulSoup
import requests


date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get("https://www.billboard.com/charts/hot-100/" + date)

soup = BeautifulSoup(response.text, 'html.parser')
song_names_spans = soup.find_all("span", class_="chart-element__information__song")
song_names = [song.getText() for song in song_names_spans]

# client_id = "d9fbf6aeb04e460db070df1ff952eacf"
# client_secret ="03ba6aff6e5e4b4c89570f4a82c9f5e6"


