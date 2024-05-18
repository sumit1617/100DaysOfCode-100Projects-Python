import pandas




data = pandas.read_csv("weather-data.csv")
print(data["temp"])



# ----DataFrames----
data_dict = data.to_dict()
print(data_dict)


# ----Series----
temp_list = data["temp"].to_list()
print(temp_list)


# avg = sum(temp_list)/len(temp_list)
# print(f"the average of temp_list is {round(avg, 2)}")

average = data["temp"].mean()
print(f"the average is {round(average, 2)}")


maximum = data["temp"].max()
print(f"the maximum temperature is {maximum}")


# Get data in colomn.
print(data["condition"])
print(data.condition)  # --> by this two method we can get the data in column


# Get data in row.
print(data[data.day == "Monday"])
print(data[data.temp == data.temp.max()])


# Data in row with condition
monday = data[data.day == "Monday"]
print(monday.condition)
print(monday.temp * 9/5 + 32)


# Create DataFrame from scratch.
data_dictionary = {
    "students" : ["Sumit", "Shubham", "Sahil"],
    "scores" : [89, 96, 99]
}

info = pandas.DataFrame(data_dictionary)
info.to_csv("students_scores.csv")




