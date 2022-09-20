# -------- How to Iterate over a Pandas Dataframe. -------

student_dict = {
    "student" : ['Sumit', 'Shubham', 'Sahil', 'Sandeep'],
    "score" : [95, 98, 96, 97]
}

# Looping Through dictionaries
# for (key, value) in student_dict.items():
#     print(key)

import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop Through data frames.
# for (key, value) in student_data_frame.items():
#     print(value)


# Loop Through rows of a data frame.
for (index, row) in student_data_frame.iterrows():
    print(row)
