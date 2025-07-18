from turtle import Turtle


start=(0,-280)
move=10
finish=280

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.shape("turtle")
    self.penup()
    self.goto(start)
    self.setheading(90)

  def go_up(self):
    self.forward(move)

  def go_to_start(self):
    self.goto(start)

  def finish(self):
    if self.ycor()>finish:
      return True
    else:
      return False
  