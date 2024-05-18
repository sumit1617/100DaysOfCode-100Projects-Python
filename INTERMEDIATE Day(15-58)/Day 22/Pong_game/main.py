from turtle import Screen, Turtle, xcor
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time



screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game")
screen.textinput(title="Rules of the Game", prompt="The player who scores 5 will win the Game. Enter a OK to start: ")
screen.tracer(0)



r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    # Detect collosion with waall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
        

    # Detect collosion with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()


    # Detect L paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


    # Make the game over when make one player wi
    if scoreboard.r_score == 5 or scoreboard.l_score == 5:
        game_is_on = False
        scoreboard.game_over()


screen.exitonclick()
