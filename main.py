import turtle
import time
from scoreboard import Scoreboard
from food import Food
from snake import Snake
screen = turtle.Screen()
screen.setup(600,600)
screen.bgcolor('black')
screen.title("KING COBRA")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(key='Up',fun=snake.up)
screen.onkey(key='Down',fun=snake.down)
screen.onkey(key='Left',fun=snake.left)
screen.onkey(key='Right',fun=snake.right)


gameon = True

while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()>280 or snake.head.ycor()<-280:
        scoreboard.game_over()
        gameon = False


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            gameon = False
            scoreboard.game_over()

screen.exitonclick()