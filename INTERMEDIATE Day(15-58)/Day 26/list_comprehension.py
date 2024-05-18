# list comprehension is creating a list from another existing list.
# [new_item for item in list]

# list
numbers = [1, 2, 3]
new_numbers = [n+1 for n in numbers]
print(new_numbers)

# string
name = "sumit"
letter_list = [letter for letter in name]
print(letter_list)

# range
range_list = [n+n for n in range(1,6)]
print(range_list)


# Conditional list comprehension
# [new_item for item in list if test]
names = ["Sumit", "Shubham", "Sahil", "Sandeep", "Krishna", "Bipin"]
short_names = [name for name in names if len(name) < 6]
long_names = [name.upper() for name in names if len(name) > 6]
print(short_names)
print(long_names)

