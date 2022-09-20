from turtle import Turtle, Screen, colormode
import random

tim = Turtle()
colormode(255)
style = ('Courier', 90, 'normal')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colours = (r, g, b)
    return colours



tim.color(random_color())
tim.write('SAHIL\nloves\nPallavi', font=style, align = 'center')
tim.hideturtle()





my_screen = Screen()
my_screen.exitonclick()