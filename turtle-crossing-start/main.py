import time
from turtle import Screen

from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, 'Up')
i = 0

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    if i == 0:
        car_manager.generate_cars()

    car_manager.move_cars()

    if player.ycor() > 260:
        player.restart()
        car_manager.next_level()
        scoreboard.update_score()

    for car in car_manager.cars:
        if player.distance(car) < 22:
            game_is_on = False
            scoreboard.game_over()

    i += 1
    if i == 15:
        i = 0
