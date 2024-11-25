from turtle import Turtle
class Paddle(Turtle):

    def __init__(self,xpos):
        super().__init__()
        self.shape("square")
        self.pu()
        self.speed(0)
        self.goto(xpos,0)
        self.color("white")
        self.shapesize(stretch_wid=5,stretch_len=1)
    
    
    def move_up(self):
        if self.ycor()<250:
            newy = self.ycor() +20
            self.goto(x= self.xcor(), y= newy)
    
    def move_down(self):
        if self.ycor()>-250:
            newy = self.ycor() -20
            self.goto(x= self.xcor(), y= newy)