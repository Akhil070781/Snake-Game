from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.goto(randint(-280,280),randint(-280,280))
        
    def refresh(self):
        self.goto(randint(-280,280),randint(-280,280))
        