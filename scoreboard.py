from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 1
        self.goto(-280, 270)
        self.write(f'Level : {self.score}', font=FONT)

    def update_scoreboard(self):
        self.clear()
        self.score += 1
        self.write(f'Level : {self.score}', font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0, 0)
        self.write('GAME OVER', align='center', font=FONT)