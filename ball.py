from turtle import Turtle
import random
import time


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.speed = 10
        self.shape("circle")
        self.color("white")
        self.pu()
        self.setheading(random.randint(10,45))
    
    def move_ball(self):
        self.forward(self.speed)
        time.sleep(0.03)
    
    def bounce(self):
        self.setheading(360-self.heading())
    #bouncing along x axis
    def bounce_X(self):
        self.setheading(180-self.heading())
        
    def reset_ball(self):
        self.goto(0,0)
        self.bounce_X()
    
    def updatespeed(self):
        self.speed +=1
    
    def resetspeed(self):
        self.speed =10