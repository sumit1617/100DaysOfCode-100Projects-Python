age = input("What is your current age?")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
x = days_remaining
y = weeks_remaining
z = months_remaining
print(f"You have {x} days, {y} weeks, and {z} months left.")