from turtle import Turtle

FONT = ("Courier", 17, "normal")


class Level(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color('white')
        self.hideturtle()
        self.level = 1
        self.update_level()

    def update_level(self):
        self.clear()
        self.sety(240)
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def next_level(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.sety(0)
        self.write(f"GAME OVER", align='center', font=FONT)

    def restart(self):
        self.level = 0
        self.update_level()
