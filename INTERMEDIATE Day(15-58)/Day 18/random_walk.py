from turtle import Turtle, Screen, colormode
import random


tim = Turtle()
colormode(255)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)
    return random_color


directions = [0, 90, 180, 270]
pen_size = [10, 11, 12, 13, 14, 15, 16]

for _ in range(200):
    tim.speed(0)
    tim.color(random_color())
    tim.pencolor(random_color())
    tim.pensize(random.choice(pen_size))
    tim.forward(30)
    tim.setheading(random.choice(directions))



my_screen = Screen()
my_screen.exitonclick()