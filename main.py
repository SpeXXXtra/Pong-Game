from turtle import Screen,Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#creating the screen 
screen = Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)#animations are now off


#create paddle and make it move up and down by 20px
paddle1 = Paddle(380)
paddle2 = Paddle(-380)
screen.onkeypress(key ='Up',fun=paddle1.move_up)
screen.onkeypress(key ='Down',fun=paddle1.move_down)
screen.onkeypress(key ='w',fun=paddle2.move_up)
screen.onkeypress(key ='s',fun=paddle2.move_down)

#the ball
ball = Ball()
score = Scoreboard()

game_is_on = True#boolean value to see if game is running  

while game_is_on:
    screen.update()#update the screen
    ball.move_ball()
    
    if ball.ycor() > 290 or ball.ycor() < -290:
        #bouncing method 
        ball.bounce()
        
    if ball.xcor()>399:
        ball.resetspeed()
        ball.reset_ball()
        score.l_point()
    
    if ball.xcor()<-390:
        ball.resetspeed()
        ball.reset_ball()
        score.r_point()
        
    if (ball.distance(paddle1) <50 and ball.xcor()>360) or (ball.distance(paddle2) <50 and ball.xcor()< -360):
        ball.bounce_X()
        ball.updatespeed()
  
    #collison on right wall
    
    

screen.exitonclick()