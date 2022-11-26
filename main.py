from turtle import Turtle,Screen

from scoreboard import scoreboard
from snake import Snake
from food import food
import time


s=Screen()
s.title("Snake Game")
s.bgcolor("black")
s.setup(600,600)
s.tracer(0)


snake=Snake()
food=food()
score=scoreboard()

s.listen()
s.onkey(snake.Up,"Up")
s.onkey(snake.Down,"Down")
s.onkey(snake.Left,"Left")
s.onkey(snake.Right,"Right")


game_is=True
while game_is:
    s.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.refresh()
        score.incr()


    #wall collision
    if snake.head.xcor() > 280 or snake.head.xcor() < -200 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is=False
        score.game_over()







    







s.exitonclick()