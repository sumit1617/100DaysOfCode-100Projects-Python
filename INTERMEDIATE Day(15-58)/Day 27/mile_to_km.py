from tkinter import *


def mile_to_km():
    miles = float(mile_input.get())
    km = 1.609 * miles
    km_label.config(text=km)





window = Tk()
window.title("Mile to Kilometers conversion")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Mile
mile = Label(text="Mile", font=("Times New Roman", 15, "bold"))
mile.place(x=30, y=30)
mile_input = Entry(width=15)
mile_input.place(x=90, y=35)


# Converter
convert = Button(text="Convert", command=mile_to_km)
convert.place(x=200, y=75)

# Kilometres
kilometer = Label(text="Kilometres", font=("Times New Roman", 15, "bold"))
kilometer.place(x=30, y=125)
km_label = Label(text=0, font=("Times New Roman", 15, "bold"))
km_label.place(x=150, y=125)




window.mainloop()
