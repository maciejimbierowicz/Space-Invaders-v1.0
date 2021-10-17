from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape('images/ship.gif')
        self.penup()
        self.goto(0, -260)
        self.showturtle()

    def move_left(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())

    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())


class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.shape('square')
        self.color('white')
        self.shapesize(stretch_len=0.1, stretch_wid=0.5)
