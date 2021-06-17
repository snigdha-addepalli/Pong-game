#Pong Game
import turtle

wn=turtle.Screen()
wn.title("Pong by Snigdha")
wn.bgcolor('black')
wn.setup(width=800, height=600)
wn.tracer(0)

#Score
score_1=0
score_2=0

#Left Paddle
paddle_left=turtle.Turtle()
paddle_left.speed(0)
paddle_left.shape('square')
paddle_left.color('white')
paddle_left.shapesize(stretch_wid=5, stretch_len=1)
paddle_left.penup()
paddle_left.goto(-350,0)

#Right Paddle
paddle_right=turtle.Turtle()
paddle_right.speed(0)
paddle_right.shape('square')
paddle_right.color('white')
paddle_right.shapesize(stretch_wid=5, stretch_len=1)
paddle_right.penup()
paddle_right.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(50)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx=2
ball.dy=-2

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write( "Player-1: {}  Player-2: {}".format(score_1,score_2), align="center",font=("Courier",24,"normal"))

#Paddle Movement
def paddle_left_up():
    y=paddle_left.ycor()
    y+=20
    paddle_left.sety(y)

def paddle_left_down():
    y=paddle_left.ycor()
    y-=20
    paddle_left.sety(y)

def paddle_right_up():
    y=paddle_right.ycor()
    y+=20
    paddle_right.sety(y)

def paddle_right_down():
    y=paddle_right.ycor()
    y-=20
    paddle_right.sety(y)

#Keyboard Binding
wn.listen()
wn.onkeypress(paddle_left_up,'w')
wn.onkeypress(paddle_left_down,'s')
wn.onkeypress(paddle_right_up,'Up')
wn.onkeypress(paddle_right_down,'Down')

#Main Game Loop
while True:
    wn.update()

    #Ball Movement
    ball.setx(ball.xcor()+ball.dx)
    ball.sety(ball.ycor()+ball.dy)

    # border check
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy*=-1

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1

    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        score_1+=1
        pen.clear()
        pen.write("Player-1: {}  Player-2: {}".format(score_1,score_2),align = "center",font = ("Courier",24,"normal") )

    if ball.xcor()<-390:
        ball.dx*=-1
        score_2+=1
        pen.clear()
        pen.write("Player-1: {}  Player-2: {}".format(score_1, score_2 ),align="center",font=("Courier",24,"normal"))

#Paddle and Ball Collision
if (ball.xcor()>340 and ball.xcor()<350)and (ball.ycor()<paddle_right.ycor()+50 and ball.ycor()>paddle_right.ycor()-50):
    ball.setx(340)
    ball.dx*=-1

if (ball.xcor()<-340 and ball.xcor()>-350)and (ball.ycor()<paddle_left.ycor()+50 and ball.ycor()>paddle_left.ycor()-50):
    ball.setx(-340)
    ball.dx*=-1