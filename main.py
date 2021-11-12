from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreBoard import Scoreboard
screen=Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong game")
screen.tracer(0)

r_paddle=Paddle((350,0))
l_paddle=Paddle((-350,0))
ball=Ball()
scoreboard=Scoreboard()

screen.listen()
screen.onkey(fun=r_paddle.move_up, key="Up")
screen.onkey(fun=r_paddle.move_down, key="Down")      #WHEN U R USING A FUNCTION AS A PARAMETER DONT UWRITE THE PARANTHESES

screen.onkey(fun=l_paddle.move_up, key="w")
screen.onkey(fun=l_paddle.move_down, key="s")


game_is_on=True     ## WHEN WE USE THE UPDATE THERE HAS TO BE A WHILE LOOP CHECKING FOR A CONDITION EG HERE GAME_IS_ON
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detecting collision with wall
    if ball.ycor()>280 or ball.ycor()<-280:
        #needs to bounce
        ball.bounce_y()
    #detect collision with r_paddle
    if ball.distance(r_paddle)<50 and ball.xcor()>320 or ball.distance(l_paddle)<50 and ball.xcor()<320:
        ball.bounce_x()

    #detect whenn  Right paddlle misses
    if ball.xcor()>380:
        ball.reset_position()
        scoreboard.l_point()
    #detect when left paddle misses
    if ball.xcor()<-380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()