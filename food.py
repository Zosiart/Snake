from turtle import Turtle
import random

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.75, stretch_wid=0.75)
        self.color("#ee9b00")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-250, 250)
        radom_y = random.randint(-250, 250)
        self.goto(random_x, radom_y)