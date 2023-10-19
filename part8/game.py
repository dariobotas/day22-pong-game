import time
from turtle import Screen

from part8.ball import Ball
from part8.paddle import Paddle
from part8.scoreboard import Scoreboard

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
#screen.onkeypress(key="Up", fun=r_paddle.up)
#screen.onkeypress(key="Down", fun=r_paddle.down)
#screen.onkeypress(key="w", fun=l_paddle.up)
#screen.onkeypress(key="s", fun=l_paddle.down)
#screen.getcanvas().bind("<Up>", r_paddle.up)
#screen.getcanvas().bind("<Down>", r_paddle.down)
#screen.getcanvas().bind("<w>", l_paddle.up)
#screen.getcanvas().bind("<s>", l_paddle.down)

print(r_paddle.pos())
print(l_paddle.pos())
game_is_on = True

while game_is_on:
  time.sleep(ball.move_speed)
  screen.update()
  ball.move()

  #detect collision with top and bottom wall
  if ball.ycor() > 250 or ball.ycor() < -250:
    ball.bounce_y()

  #detect collision with r_paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.bounce_x()

  #if paddle is not reflect by any paddle
  if ball.xcor() > 380:
    ball.reset_position()
    scoreboard.l_point()

  if ball.xcor() < -380:
    ball.reset_position()
    scoreboard.r_point()

screen.exitonclick()
