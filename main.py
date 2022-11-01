import turtle
from turtle import Screen
from icon import Player
from bus import Bus
import time
from score import Score

screen = Screen()
screen.bgcolor("white")
screen.setup(600, 600)
screen.title("TURTLE CROSSING")

screen.tracer(0)
score=Score()
screen.listen()
player = Player()
screen.onkey(player.upkey, "Up")
bus = Bus()
game = True
while game:
    time.sleep(0.1)
    screen.update()
    bus.movement()
    bus.move()
    if player.ycor() > 260:
        score.incerement()
        player.is_game_over()
        bus.levelup()

    for car in bus.all_cars:
        if player.distance(car) < 20:
            player.end()
            game = False

screen.exitonclick()
