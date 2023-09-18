import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=1200, height=600)
screen.bgcolor('grey')
screen.tracer(0)

marking1 = Turtle()
marking1.penup()
marking1.shape('square')
marking1.shapesize(1, 100)
marking1.color('black')
marking1.sety(75)

marking2 = Turtle()
marking2.penup()
marking2.shape('square')
marking2.shapesize(1, 100)
marking2.color('black')
marking2.sety(-75)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move, 'Up')
screen.onkey(player.back, 'Down')

game_is_on = 0
while game_is_on!=-1:
    game_is_on += 1
    time.sleep(0.001)
    screen.update()
    if game_is_on % 2:
        car_manager.create_car()
    car_manager.move_cars()

    # Detect accident
    for car in car_manager.cars:
        if car.distance(player) < 25:
            game_is_on = -1

    # Detect a successful crossing
    if player.ycor() > 280:
        player.goto_start()
        car_manager.level_up()
        scoreboard.update_scoreboard()

scoreboard.game_over()

screen.exitonclick()
