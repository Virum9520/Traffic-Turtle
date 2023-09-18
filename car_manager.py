from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 3
MOVE_INCREMENT = 2


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        rc = random.randint(1,6)
        if rc == 6:
            car = Turtle()
            car.shape('square')
            car.shapesize(1, 2)
            car.color(random.choice(COLORS))
            car.penup()
            car.seth(180)
            car.goto(560, random.randint(-230, 250))
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

