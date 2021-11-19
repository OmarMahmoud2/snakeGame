import turtle
import time 

postions = [(0,0), (-20, 0), (-40, 0)]

dist = 20
up = 90 
right = 0 
down = 270 
left = 180 

class Snake:
  
  def __init__(self):
    self.snake = []
    self.create_snake()
    self.head = self.snake[0]
    self.tail = self.snake[-1]
    
  def create_snake(self):
    for postion in postions:
      self.elongate(postion)
    
  def elongate(self, postion):
    alex = turtle.Turtle('square')
    alex.color('white')
    alex.penup()
    alex.speed(1)
    alex.goto(postion)
    self.snake.append(alex)
  
  def extend(self):
    self.elongate((self.tail.xcor() + 20 , self.tail.ycor() + 20))

  def tail_hit(self):
    if self.head.distance(self.tail) < 5:
      print('tail hit')
      return True
    else:
      for turt in self.snake[1: ]:
        if self.head.distance(turt) < 5:
          print('body hit')
          return True 
        else:
          pass
    
  def move(self):
      for num in range(len(self.snake) -1, 0, -1):
        newX = self.snake[num - 1].xcor()
        newY = self.snake[num - 1].ycor()
        self.snake[num].goto(newX, newY)
    
      self.head.forward(dist)
      self.head.speed(1)
  
  
  def resset(self):
    for turt in self.snake[3:]:
      turt.hideturtle()
    del self.snake[3: ]
    
    
  def up(self):
    if self.head.heading() == down:
      pass
    else:
      self.head.setheading(up)
    
  def down(self):
    if self.head.heading() == up:
      pass
    else:
      self.head.setheading(down)
  
  def right(self):
    if self.head.heading() == left:
      pass
    else:
      self.head.setheading(right)
  
  def left(self): 
    if self.head.heading() == right:
      pass
    else:
      self.head.setheading(left)
    
  