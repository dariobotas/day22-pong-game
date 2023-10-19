from turtle import Turtle


class Ball(Turtle):

  def __init__(self, position):
    super().__init__()
    self.shape("circle")
    self.color("white")
    self.shapesize(0.5)
    self.penup()
    self.goto(position)

  def move(self):
    new_x = self.xcor() + 10
    new_y = self.ycor() + 10
    self.goto(new_x,new_y)

 