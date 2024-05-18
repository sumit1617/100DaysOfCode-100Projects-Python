def calculate(n, **kwargs):
    print(kwargs)
    print(f"the starting value of n is = {n}")
    n += kwargs["add"]
    print(f"the value of n after adding 3 is = {n}")
    n *= kwargs["multiply"]
    print(f"the value of n after multiplying 5 is = {n}")


calculate(2, add=3, multiply=5)


# The kwargs(**kwargs) means like it is dictionary.


# let's create our own class and give **kwargs function.
class food:

    def __init__(self, **kw):
        self.starters = kw.get("starters")
        self.main_course = kw.get("main_course")
        self.deserts = kw.get("deserts")
        self.fast_food = kw.get("fast_food")
        self.drinks = kw.get("drinks")


my_food = food(starters="pizza")
print(my_food.starters)

