def add(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(add(2, 3, 5))

# the argument(*args) function is used to take infinite no of inputs.
# We can write anything after the star-mark(*).
