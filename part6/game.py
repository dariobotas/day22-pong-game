import time
from turtle import Screen

from part6.ball import Ball
from part6.paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

l_paddle = Paddle((-380, 0))
r_paddle = Paddle((380, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

print(r_paddle.pos())
print(l_paddle.pos())
game_is_on = True

while game_is_on:
  time.sleep(0.2)
  screen.update()
  ball.move()

  #detect collision with top and bottom wall
  if ball.ycor() > 250 or ball.ycor() < -250:
    ball.bounce()

  #detect collision with r_paddle
  if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
    ball.reflect()

  #if paddle is not reflect by any paddle
  #if ball.distance(l_paddle) <= -280:
  #  ball.reflect()

screen.exitonclick()
