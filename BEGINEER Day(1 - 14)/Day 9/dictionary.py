programming_dictionary = {
    "Bug" : "An error in a program that prevents the program from running as expected",
    "Function" : "A peice of code that you can easily call over and over again",
}

# Retrieving items from dictionary
# print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loops"] = "The action of doing something over and over again."

# Creating an empty dictionary
# empty_dictionary = {}

# # Wipe an existing dicctionary
# programming_dictionary = {}

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"

# Loop through a dictionary
for key in programming_dictionary:
    print(key)
    print(programming_dictionary[key])


#  NESTING
capitals = {
    "Maharashtra" : "Mumbai",
    "Goa" : "Panaji",
    "UP": "Lucknow",
}

# Nesting list in dictionary
travel_log = {
    "Maharashtra" : ["Mumbai","Pune","Ratnagiri"],
    "UP" : ["Varanasi","Kanpur","Lucknow"],
}

# Nesting Dictionary in dictionary
travel_log = {
    "Maharashtra" : {"cities_visited":["Mumbai","Pune","Ratnagiri"],"total_visits" : 12},
    "UP" : ["Varanasi","Kanpur","Lucknow"],
}

# Nesting dictionary in a lists
travel_log = [
    {
        "State" : "Maharashtra", 
    "cities_visited":["Mumbai","Pune","Ratnagiri"],
     "total_visits" : 12
    },
    {
        "State" : "UP", 
        "cities_visited":["Varanasi","Kanpur","Lucknow"],
         "total_visits": 6
    },
]