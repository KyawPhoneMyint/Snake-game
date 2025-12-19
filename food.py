from turtle import Turtle
import random as rnd
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5,0.5)
        self.color("blue")
        self.speed(0)
        self.refresh()

    def refresh(self):
        self.goto(rnd.randint(-200, 200), rnd.randint(-200, 200))