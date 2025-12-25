from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score=0
        with open("score_highest.txt","r") as f:
            self.high_score=int(f.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0,240)
        self.score_show()

    def increase_count(self):
        self.score+=1
        self.score_show()

    def score_show(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}", move=False, align="center", font=("Courier", 28, "bold"))

    def reset_score(self):
        if self.score>self.high_score:
            self.high_score=self.score
            with open("score_highest.txt","w") as f:
                f.write(str(self.high_score))
        self.score=0
        self.score_show()