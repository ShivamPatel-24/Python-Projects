from turtle import * 
import random

timmy = Turtle()
timmy.shape("turtle")
timmy.color("red")

timmy.speed("fast")
timmy.pensize(10) 

colormode(255)
timmy.de

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def draw_shapes():
    for i in range(3, 11):
        timmy.pencolor(random_color())
        for j in range(i):
            timmy.forward(100)
            timmy.right(360//i)


def random_walk():
    for i in range(75):
        r = random.choice([0, 1, 2])
        timmy.pencolor(random_color())
        timmy.forward(30)
        timmy.right(random.choice([90, 180, 270, 360]))    
        

def spiro_graph():
    timmy.speed("fastest")
    timmy.pensize(1)
    
    for i in range(72):
        timmy.pencolor(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + 5)
    

# random_walk()
# draw_shapes()
spiro_graph()


screen = Screen()
screen.exitonclick()