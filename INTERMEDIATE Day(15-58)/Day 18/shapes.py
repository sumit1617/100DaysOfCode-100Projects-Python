from turtle import Turtle, Screen
import random

colours = ["deep sky blue", "firebrick", "yellow", "black", "blue", "navy", "red", "green", "pink", "magenta", "grey","brown", "lime"]
tim = Turtle()

def draw_shape(number_sides):
    angle = 360 / number_sides
    for _ in range(number_sides):
        tim.forward(100)
        tim.right(angle)

for num_sides in range(3, 11):
    tim.color(random.choice(colours))
    draw_shape(num_sides)



my_screen = Screen()
my_screen.exitonclick()