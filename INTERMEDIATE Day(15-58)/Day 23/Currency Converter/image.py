from tkinter import *
from PIL import Image, ImageTk

currency_root = Tk()

currency_root.geometry("500x500")
# photo = PhotoImage(file="pina-messina-Sw2XNTgA-wc-unsplash.jpg")

# for JPG images
image = Image.open("currency.jpg")
photo = ImageTk.PhotoImage(image)



currency_lable = Label(image=photo)
currency_lable.pack()


currency_root.mainloop()