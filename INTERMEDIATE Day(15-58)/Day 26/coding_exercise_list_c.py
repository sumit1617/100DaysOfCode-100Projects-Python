# squared the numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n*n for n in numbers]
print(squared_numbers)

# print the even numbers
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)


# print the common number from both the file1 and file2.
with open("file1.txt") as file1:
    file_1_data = file1.readlines()

with open("file2.txt") as file2:
    file_2_data = file2.readlines()

result = [int(n) for n in file_1_data if n in file_2_data]
print(result)
