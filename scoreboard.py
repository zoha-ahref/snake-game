from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "bold")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.scores = 0
        self.color("white")
        self.penup()
        self.goto(x=-10, y=260)
        self.hideturtle()
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score = {self.scores} ", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.scores += 1
        self.clear()
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

