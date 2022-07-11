from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(800, 600)
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

is_On = True
while is_On:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #Detect R paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_points()

    #Detect L paddle misses:
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_points()

    # if ball.xcor() > 380:
    #     #is_On = False
    #     ball.reset_position()
    #     scoreboard.l_points()
    # elif ball.xcor() < -380:
    #     ball.reset_position()
    #     scoreboard.r_points()
        
    # if ball.distance(r_paddle) < 50 and ball.xcor() > 340:
    #     ball.bounce_x()
    #     scoreboard.r_points()
    
    # if ball.distance(l_paddle) < 50 and ball.xcor() < -340:
    #     ball.bounce_x()
    #     scoreboard.l_points()

screen.exitonclick()