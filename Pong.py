import turtle
import time
from time import sleep
import random
import winsound

wn = turtle.Screen()
wn.title("Frankies ding dong")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)
# menu= turtle.Screen()

# menu.title("Menu")
# menu.bgcolor("black")
# menu.setup(width=300, height=200)
# menu.tracer(0) 
# menu.title




#score
score_a = (0)
score_b = (0)

#paddle 
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("red")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)
#paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("pink")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(+350, 0)
#ball
# def ballanglechanger():
#     yvariantspeed = [1.8,1.9,2,2.1,2.2,2.3]
#     ballspeedy = random.sample(yvariantspeed,1)[0]
#     print (ballspeedy)
#     return ballspeedy
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("green")
ball.penup()
ball.goto(0, 0)
ballspeedx= 2
# ballspeedy = ballanglechanger()
ballspeedy = 2
print(ballspeedy)
print(type(ballspeedy))
ball.dx = ballspeedx
ball.dy = ballspeedy

#Scoreboard Text
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Cuckold A: 0  Cuckold B: 0", align="center", font=("Courier", 24,"normal"))

#paddle movements
movement_speed = 20
def paddle_a_up():
    y = paddle_a.ycor()
    y += movement_speed
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -=movement_speed
    paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    y += movement_speed
    paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    y -=movement_speed
    paddle_b.sety(y)
#onkeypress
wn.listen()
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
#ball move
def yaxis_collision_handler () :
    ball.dy *=-1
def xaxis_collision_handler () :
    global score_a, score_b
    ball.dx *=-1
    ball.goto(0, 0)
    #ballspeedy = ballanglechanger()
def check_ball_position () :
    global score_a, score_b
    if ball.ycor() > 290:
        yaxis_collision_handler()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    if ball.ycor() < -290:
        yaxis_collision_handler()
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() > 390:
        xaxis_collision_handler()
        score_a +=1
        pen.clear()
        pen.write("Cuckold A: {}  Cuckold B: {}".format(score_a, score_b), align="center", font=("Courier", 24,"normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    if ball.xcor() < -390:
        xaxis_collision_handler()
        score_b +=1
        pen.clear()
        pen.write("Cuckold A: {}  Cuckold B: {}".format(score_a, score_b), align="center", font=("Courier", 24,"normal"))
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
 #ball movement
def ball_handler() :
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #border
    check_ball_position()

    #Paddle collision
    if (ball.xcor() > 330 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() -50 ):
        ball.setx (330)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    if (ball.xcor() < -330 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() -50 ):
        ball.setx (-330)
        ball.dx *=-1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

        

#main game loop
while True:
        
    ball_handler()
    wn.update()
    sleep(.015)

# if dy is 0.7 dy -0.7