#  Function that allow for 1 input
#  Parameter ---> it is the name of the data which is inside the def function eg:- name
#  Argument ---> it is the actual peice of data eg:- sumit

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How are you {name}? ")
    print(f"Hey! {name} Come & play with us")

name  = input("Type your name: ")
greet_with_name(name)

