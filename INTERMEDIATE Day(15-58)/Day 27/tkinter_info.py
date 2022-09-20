from tkinter import *

window = Tk()
window.title("tkinter more information")
window.minsize(width=500, height=500)


# Text
text = Text(height=5, width=30)
# Puts cursor in text box
text.focus()
# Add some text to begin with.
text.insert(END, "Example of multi-line text entry.")
# Get current value in textbox at line 1, character 0
print(text.get("1.0", END))
text.pack()


# SpinBox
def spinbox_used():
    # gets the current values in spinbox
    print(spinbox.get())


spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spinbox.pack()


# Scale
# Called with current scale value.
def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


# CheckButton
def checkbutton_used():
    # Prints 1 if On button checked, otherwise 0
    print(checked_state.get())


checked_state = IntVar()
checkbutton = Checkbutton(text="Is on?", variable=checked_state, command=checkbutton_used)
checked_state.get()
checkbutton.pack()


# RadioButton
def radio_used():
    print(radio_state.get())


# Variable to hold on to which radio button value is checked
radio_state = IntVar()
radiobutton1 = Radiobutton(text="Option-1", value=1, variable=radio_state, command=radio_used)
radiobutton2 = Radiobutton(text="Option-2", value=2, variable=radio_state, command=radio_used)
radiobutton1.pack()
radiobutton2.pack()


# List
def listbox_used(event):
    # Gets  current selection from list box
    print(listbox.get(listbox.curselection()))


listbox = Listbox(height=4)
foods = ["Pizza", "Sandwich", "Coke", "Ice-cream"]
for items in foods:
    listbox.insert(foods.index(items), items)

listbox.bind("<<ListboxSelect>>", listbox_used)
listbox.pack()


window.mainloop()