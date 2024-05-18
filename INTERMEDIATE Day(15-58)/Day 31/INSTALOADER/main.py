import instaloader
from PIL import Image, ImageTk
import os


loader = instaloader.Instaloader()
user = input("Enter username: ")
loader.download_profile(user, profile_pic= True)
img = [x for x in os.listdir(f'{os.getcwd()}/{user}') if x.endswith("jpg")]
img = Image.open(f'{os.getcwd()}/{user}/{img[0]}')
img.show()