from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.count=0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,240)
        self.score_show()

    def increase_count(self):
        self.count+=1
        self.clear()
        self.score_show()

    def score_show(self):
        self.write(f"Score:{self.count}",move=False,align="center",font=("Courier",28,"bold"))

    def game_over(self):
        self.home()
        self.write("Game over",move=False,align="center",font=("Courier",28,"bold"))
