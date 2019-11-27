# Simple Pong in Python3
# Used "turtle module"

import turtle
import os

player1score = 0
player2score = 0

wn = turtle.Screen()
wn.title("PONG")
wn.bgcolor("black")
wn.setup(width = 1280, height = 720)
wn.tracer(0)

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_a.penup()
paddle_a.goto(-600, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid = 5, stretch_len = 1)
paddle_b.penup()
paddle_b.goto(600, 0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.25
ball.dy = 0.25

# Score Card
card = turtle.Turtle()
card.speed(0)
card.color("white")
card.penup()
card.hideturtle()
card.goto(0, 320)
card.write("Player A: 0      Player B: 0", align = "center", font = ("New Baskerville", 24, "normal"))


# Functions

# Moving the paddle_a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 25
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 25
    paddle_a.sety(y)

# Moving the paddle_b
def paddle_b_up():
    y = paddle_b.ycor()
    y += 25
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 25
    paddle_b.sety(y)


# Key bindings
wn.listen()

# For paddle_a
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

# For paddle_b
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


# Main game loop
while True:
    wn.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Ball Bounce boundary
    if ball.ycor() > 350:
        ball.sety(350)
        ball.dy *= (-1)
        os.system("aplay bounce.wav&")
    
    if ball.ycor() < -350:
        ball.sety(-350)
        ball.dy *= (-1)
        os.system("aplay bounce.wav&")
    
    # Ball bounce paddle
    if (ball.xcor() < -590 and ball.xcor() > -600) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-590)
        ball.dx *= (-1)
        os.system("aplay bounce.wav&")
        #ball.dy *= (-1)

    if (ball.xcor() > 590 and ball.xcor() < 600) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(590)
        ball.dx *= (-1)
        os.system("aplay bounce.wav&")
        #ball.dy *= (-1)

    # Score
    if ball.xcor() > 630:
        ball.goto(0, 0)
        ball.dx *= (-1)
        player1score += 1
        card.clear()
        card.write("Player A: {}      Player B: {}".format(player1score, player2score), align = "center", font = ("New Baskerville", 24, "normal"))

    if ball.xcor() < -630:
        ball.goto(0, 0)
        ball.dx *= (-1)
        player2score += 1
        card.clear()
        card.write("Player A: {}      Player B: {}".format(player1score, player2score), align = "center", font = ("New Baskerville", 24, "normal"))

