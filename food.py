import turtle 
import random



class Food(turtle.Turtle):
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.penup()
    y = random.randint(-180, 180)
    x = random.randint(-180, 180)
    self.goto(x, y)
    self.shapesize(stretch_len = 0.5, stretch_wid = 0.5)
    self.color('blue')
    
  def collide(self):
    nx = random.randint(-180, 180)
    ny = random.randint(-180, 180)
    self.goto(nx, ny)
    
    