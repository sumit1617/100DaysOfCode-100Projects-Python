states_of_india = ["Maharashtra","Delhi","UK","UP","Bihar","Gujarat","Rajasthan"]

# it will the print the satates that is on the position 1. in computer you know that the countinng is start from 0
# print(states_of_india[1])

# we can also update the list
states_of_india[2] = "UttaraKhand"
states_of_india[3] = "Uttar Pradesh"

# we can also add the item into the list
states_of_india.append("Goa")

#the above one will add ony single item to list. But below one can add n numbers of items to the list
states_of_india.extend(["Harayana","Tamil Nadu","Kerala","Hyderabad"])

#it uses to insert an item at a given position
states_of_india.insert(1, "Punjab")

#it uses to remove the item from the list
states_of_india.remove("Punjab")

#  it remove the item at the given position in the list, and return it. if no index is specified
states_of_india.pop()

# it uses to clear the list
# states_of_india.clear()

#it uses to pprint the position of item
print(states_of_india.index('Goa'))

#it uses to count the number of items appears in the list
print(states_of_india.count('Goa'))

#it uses to reverse the list
states_of_india.reverse()

#it uses to sort the list
states_of_india.sort()

#it returns a shalllow copy of the list 
print(states_of_india.copy())


print(states_of_india)