from turtle import Turtle, Screen, circle

tim = Turtle()
screen = Screen()


def set_heading90():
    tim.setheading(90)

def set_heading0():
    tim.setheading(0)

def set_heading180():
    tim.setheading(180)

def set_heading270():
    tim.setheading(270)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def move_forward():
    tim.forward(25)

def move_backward():
    tim.backward(25)

def clockwise():
    for _ in range(1):
        tim.right(90)
        tim.right(90)
        tim.right(90)
        tim.right(90)

def anti_clockwise():
    for _ in range(1):
        tim.left(90)
        tim.left(90)
        tim.left(90)
        tim.left(90)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key="f", fun=move_forward)
screen.onkey(key="b", fun=move_backward)
screen.onkey(key="a", fun=anti_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear_screen)
screen.onkey(key="o", fun=circle)
screen.onkey(key="n", fun=set_heading90)
screen.onkey(key="w", fun=set_heading180)
screen.onkey(key="s", fun=set_heading270)
screen.onkey(key="e", fun=set_heading0)  
screen.onkey(key="l", fun=turn_left)
screen.onkey(key="r", fun=turn_right) 
screen.exitonclick()
