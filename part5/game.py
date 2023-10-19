import time
from turtle import Screen

from part5.ball import Ball
from part5.paddle import Paddle

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

game_is_on = True

while game_is_on:
  time.sleep(0.05)
  screen.update()
  ball.move()

  if ball.ycor() > 210 or ball.ycor() < -210:
    ball.bounce()
  
    

screen.exitonclick()
