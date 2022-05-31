import turtle

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

while True:
    ball.sety(ball.ycor() - 1)

