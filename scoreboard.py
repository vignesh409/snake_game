from turtle import Turtle


class scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"score:{self.score}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align="center",font=("Courier", 20, "normal"))

    def incr(self):
        self.score += 1
        self.clear()
        self.update()
