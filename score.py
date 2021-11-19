from turtle import Turtle 

file = open('hi.txt', 'r')
cont = file.read()
if cont.isnumeric():
  p = int(cont) 
file.close()

class Score(Turtle):
 
  def __init__(self):
    super().__init__()
    self.shape('circle')
    self.hideturtle()
    self.clear()
    self.penup()
    self.pencolor('white')
    self.score = 0
    self.hscore = p
    self.goto(0, 170)
    self.write(f'Score: {self.score}. Highest score: {self.hscore}', move = False, align = 'center', font=("Arial",15,"normal"))
 
 
  def up(self):
    self.clear()
    self.score += 1
    self.write(f'Score: {self.score}. Highest score: {self.hscore}', move = False, align = 'center', font=("Arial",15,"normal"))
    
      
  def resset(self):
    if self.score > self.hscore:
      self.hscore = self.score
      file = open('hi.txt', 'w')
      file.write(str(self.hscore))
      file.close()
    self.score = 0 
    self.clear()
    self.write(f'Score: {self.score}. Highest score: {self.hscore}', move = False, align = 'center', font=("Arial",15,"normal"))

 