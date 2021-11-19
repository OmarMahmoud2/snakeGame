from turtle import Turtle

class Border(Turtle):
  def __init__(self):
    super().__init__()
    self.penup()
    self.goto(-250,0)
    self.pendown()
    self.pencolor('white')
    self.setheading(90)
    self.forward(200)
    self.right(90)
    self.forward(500)
    self.right(90)
    self.forward(400)
    self.right(90)
    self.forward(500)
    self.right(90)
    self.forward(200)  
    self.hideturtle()