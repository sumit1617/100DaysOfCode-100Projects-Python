sum_of_even = 0
for number in range(0, 101):
    if number % 2 == 0:
        sum_of_even += number

print(f"The sum of even numbers from 1 to 100 is: {sum_of_even}")

sum_of_odd = 0
for odd_number in range(0, 101):
    if odd_number % 2 != 0:
        sum_of_odd += odd_number

print(f"The sum of odd numbers from 1 to 100 is: {sum_of_odd}")

print(f"the sum of 1 to 100 is: {sum_of_odd + sum_of_even}")