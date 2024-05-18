# The below function is used to read the data from the file.
# by writing with we don't need to write close function like file.close()
with open("D:/Python Codes/Day 24/my_file.txt") as file:  # Here the absolute path method is used.

    contents = file.read()
    print(contents)


# The below function is used to write the data inside the file.
with open("my_file.txt", mode="a") as file:
    file.write("\nI'll suggest everyone to use Pycharm for the python.")
#
#
# The below function is used to create the file and write data in it.
with open("my_new_file.txt", mode="w") as file:
    file.write("My new file data.")


# The only difference between the last two function is the mode.
# Whatever we want to do with file is only we have to change the mode
