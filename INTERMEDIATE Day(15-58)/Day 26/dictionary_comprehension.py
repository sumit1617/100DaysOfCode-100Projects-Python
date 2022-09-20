# dictionary comprehension is creating a dictionary from another existing dictionary or list.


# new_dict = {new_key:new_value for item in list}
import random
names = ["Sumit", "Shubham", "Sahil", "Sandeep", "Krishna", "Bipin"]
students_scores = {student:random.randint(50,100) for student in names}
print(students_scores)
# new_dict  = {new_key:new_value for (key,value) in dict.items()}

# new_dict  = {new_key:new_value for (key,value) in dict.items() if test}
passed_students = {student:score for (student, score) in students_scores.items() if score >=65}
print(passed_students)
