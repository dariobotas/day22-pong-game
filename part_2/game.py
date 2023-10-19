from turtle import Screen
from part_2.paddle import Paddle

screen = Screen()
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("My pong game")
screen.tracer(0)

paddle1 = Paddle(-380,0)
paddle2 = Paddle(380, 0)

screen.listen()
screen.onkey(paddle1.up, "Up")
screen.onkey(paddle1.down, "Down")
screen.onkey(paddle2.up, "w")
screen.onkey(paddle2.down, "s")

game_is_on = True

while game_is_on:
  screen.update()

screen.exitonclick()
