from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake = []
        self.heading=[0,90,180,270]
        self.create_snake()
        self.head=self.snake[0]

    def create_snake(self):
        x = 0
        for i in range(3):
            turtle = Turtle("square")
            turtle.color("white")
            turtle.penup()
            turtle.goto(x, 0)
            x += -20
            self.snake.append(turtle)

    def add_segment(self):
        x=self.snake[len(self.snake)-1].xcor()-20
        y=self.snake[len(self.snake)-1].ycor()-20
        new_segment=Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(x,y)
        self.snake.append(new_segment)

    def move(self):
        for segment in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segment - 1].xcor()
            new_y = self.snake[segment - 1].ycor()
            self.snake[segment].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        if self.head.heading()!=self.heading[3]:
            self.head.setheading(self.heading[1])

    def down(self):
        if self.head.heading()!=self.heading[1]:
            self.head.setheading(self.heading[3])

    def right(self):
        if self.head.heading()!=self.heading[2]:
            self.head.setheading(self.heading[0])

    def left(self):
        if self.head.heading()!=self.heading[0]:
            self.head.setheading(self.heading[2])

    def reset(self):
        for segment in self.snake:
            segment.reset()
        self.snake.clear()
        self.create_snake()
        self.head=self.snake[0]
