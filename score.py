from turtle import Turtle
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.hideturtle()
        self.penup()
        self.goto(-150, 200)
        self.level = 0
        self.level1()
    def level1(self):
        self.clear()
        self.write(f"LEVEL:{self.level}", False, "center", ("arial", 20, "normal"))
        self.color("black")

    def incerement(self):
        self.level += 1
        self.level1()
