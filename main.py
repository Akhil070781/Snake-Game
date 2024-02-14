from turtle import Screen
import time
from food import Food
from scoreboard import Scoreboard
import snake

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
screen.listen()

snake=snake.Snake()
food=Food()
scoreboard=Scoreboard()

screen.onkey(fun=snake.up,key="Up")
screen.onkey(fun=snake.right,key="Right")
screen.onkey(fun=snake.left,key="Left")
screen.onkey(fun=snake.down,key="Down")
 
game_is_on=True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    
    if snake.head.distance(food)<15:
        food.refresh()
        scoreboard.update()
        snake.add_end()
        
    if snake.head.xcor()<-290 or snake.head.xcor()>290 or snake.head.ycor()<-290 or snake.head.ycor()>290:
        scoreboard.reset()
        snake.reset()
        scoreboard.write_score()
        
    for segments in snake.snake[1:]:
        if snake.head.distance(segments)<10:
            scoreboard.reset()
            snake.reset()
            scoreboard.write_score()

    
    
    
    
screen.exitonclick()
    