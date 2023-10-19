from part3.paddle import Paddle
from part3.paddle2 import Paddle2
from turtle import Screen

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

l_paddle = Paddle(-380, 0)
r_paddle = Paddle2((380, 0))

screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")

game_is_on = True

while game_is_on:
  screen.update()

screen.exitonclick()
