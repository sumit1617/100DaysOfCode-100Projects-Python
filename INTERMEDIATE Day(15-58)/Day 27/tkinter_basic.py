from tkinter import *  # it imports all the properties of tkinter


def change_label():
    new_label = input.get()
    my_label.config(text=new_label)


window = Tk()  # To open the screen
window.title("Sumit Kumar Singh")
window.minsize(width=500, height=300)
window.config(padx=100,pady=200)


# Label
my_label = Label(text="Sumit", font=('Arial', 18))
# my_label.place(x=0, y=0)
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)



# Button
button = Button(text="Click Me", command=change_label)
# button.place(x=200,y=50)
button.grid(column=1, row=1)
new_button = Button(text="dabao mujeh", command=change_label)
new_button.grid(column=2, row=0)


# Entry
input = Entry(width=15)
# input.place(x=100,y=100)
input.grid(column=3,row=2)
input.get()




window.mainloop()  # To hold the screen
