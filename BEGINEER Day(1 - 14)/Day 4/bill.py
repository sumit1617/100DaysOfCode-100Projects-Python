import random

#Split string method
names_string = input("Give me everbody's names, separated by a comma. \n")
names = names_string.split(", ")

num_items = len(names)
random_choice = random.randint(0, num_items - 1)
person_who_will_pay = names[random_choice]

print(person_who_will_pay + " is going to + buy a meal toady")