from turtle import Turtle
import time
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
CAR_START_X = 350


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.speed = STARTING_MOVE_DISTANCE
        self.cars = []
        self.hideturtle()

    def create_car(self):
        car = Car()
        car.color(random.choice(COLORS))
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.penup()
        car.goto(CAR_START_X, random.randint(-250, 250))
        self.cars.append(car)

    def generate_cars(self):
        n_cars = random.randint(3, 8)
        for _ in range(n_cars):
            self.create_car()

    def move_cars(self):
        for car in self.cars:
            new_x = car.xcor() - self.speed
            car.goto(new_x, car.ycor())

    def next_level(self):
        for car in self.cars:
            car.clear()
            car.hideturtle()
        self.cars = []
        time.sleep(0.5)
        self.speed += MOVE_INCREMENT
        self.generate_cars()


class Car(Turtle):
    def __init__(self):
        super().__init__(shape="square")
