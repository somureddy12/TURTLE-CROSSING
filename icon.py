from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.starting = (0, -280)
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.setheading(90)
        self.goto(self.starting)

    def upkey(self):
        self.penup()
        y = self.ycor() + 10
        self.goto(self.xcor(), y)

    def is_game_over(self):
            self.goto(self.starting)
    def end(self):
        self.goto(0,0)
        self.write("YOU LOSE", False, "center", ("arial", 20, "normal"))
