print("Welcome to Tip Calculator")
total_bill = input("what was the total bill? $")
tip_percentage = input("What percentage tip would you like to give? 10, 12 or 15? ")
total_people = input("How many people to spilt the bill? ")
tip_percentage_as_float = int(tip_percentage)
x = float(total_bill)
y = float(tip_percentage_as_float/100)
z = int(total_people)

result = ((x*y)+x)/z
final_amount = round(result,2)
final_amount = "{:.2f}".format(final_amount)
print(f"Each people should pay: ${final_amount}")
