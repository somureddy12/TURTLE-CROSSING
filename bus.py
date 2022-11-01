from turtle import Turtle
import random

MOVE = 5
INCREMENT = 5


class Bus(Turtle):
    def __init__(self):

        self.all_cars = []

        self.move1 = MOVE

    def movement(self):
        color = ["red", "yellow", "blue", "green", "violet", "pink", "purple"]
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new = Turtle(shape="square")
            new.penup()
            new.color(random.choice(color))
            new.shapesize(stretch_wid=1, stretch_len=2)
            new.goto(300, random.randint(-250, 250))
            self.all_cars.append(new)

    def move(self):
        for car in self.all_cars:
            car.backward(self.move1)

    def levelup(self):
        self.move1 += INCREMENT
