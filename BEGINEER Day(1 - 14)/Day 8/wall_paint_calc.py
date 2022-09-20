import math

test_h = int(input("Height of wall: "))
test_w = int(input("Weight of wall: "))
coverage = 5

def paint_calc(height, weight, cover):
    area = test_h * test_w
    number_of_cans = math.ceil(area / coverage)
    print(f"You'll need {number_of_cans} paints")
    
paint_calc(weight=test_h, cover=coverage, height=test_h)