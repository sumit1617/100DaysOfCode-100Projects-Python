student_height = input("Input a list of heights of students.\n").split()

for n in range(0, len(student_height)):
    student_height[n] = int(student_height[n])

# print(student_height)

total_height = 0
for height in student_height:
    total_height += height

number_of_students = 0
for students in student_height:
    number_of_students += 1

average_height = round(total_height / number_of_students)
print(f"the average height of student is: {average_height}")
