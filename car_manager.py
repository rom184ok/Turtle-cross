from turtle import Turtle
import random

colors=["red","orange","yellow"]
start=5
move=10

class CarManager(Turtle):
  def __init__(self):
    self.cars=[]
    self.speed=start

  def create_cars(self):
    rand_chance=random.randint(1,6)
    if rand_chance==1:
      car=Turtle("square")
      car.shapesize(stretch_wid=1,stretch_len=2)
      car.penup()
      car.color(random.choice(colors))
      rand_y=random.randint(-250,250)
      car.goto(300,rand_y)
      self.cars.append(car)


  def move_cars(self):
    for car in self.cars:
      car.backward(self.speed)

  def level_up(self):
    self.speed+=move

