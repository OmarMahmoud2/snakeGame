import turtle 
import time 
from snake import Snake
from food import Food 
from border import Border
from score import Score 

wn = turtle.Screen()
wn.bgcolor('black')
wn.setup(400, 400)
wn.title('My snake game')
wn.tracer(0)

snake = Snake()
food = Food()
score = Score()
border = Border()

wn.listen()
wn.onkey(snake.up, 'Up')
wn.onkey(snake.down, 'Down')
wn.onkey(snake.right, 'Right')
wn.onkey(snake.left, 'Left')



wn.update()

game_is_on = True 


while game_is_on:
  wn.update()
  time.sleep(0.2)
  snake.move()
  if snake.head.xcor() > 250 or snake.head.xcor() < -250 :
    snake.head.home()
    score.resset()
    snake.resset()
    continue
  elif snake.head.ycor() > 200 or snake.head.ycor() < -200 :
    snake.resset()
    snake.head.home()
    score.resset()
    continue
  elif snake.tail_hit():
    snake.head.home()
    snake.resset()
    score.resset()
    continue
    
  else:
    if snake.head.distance(food) < 20:
      food.collide()
      score.up()
      snake.extend()
    else: 
      pass 
    
    