from turtle import Screen
import time
from Snake import Snake
from food import Food
from score_board import Scoreboard

screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")
game_on=True

while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detection with food
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_count()
        snake.add_segment()

    #Detection with wall
    if snake.head.xcor()>280 or snake.head.xcor()<-280 or snake.head.ycor()<-280 or snake.head.ycor()>280:
        scoreboard.reset_score()
        snake.reset()

    other_segment=snake.snake[1:]
    for segment in other_segment:
        if snake.head.distance(segment) < 10:
            scoreboard.reset_score()
            snake.reset()
screen.mainloop()