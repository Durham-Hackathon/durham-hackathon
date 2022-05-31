import turtle

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

# Earth's gravitational constant
g = -9.81

# Timestep size
t = 0.008

# Starting velocity
u = 0 

while True:
    u += g*t  # update velocity in-place
    ball.sety(u*t + ball.ycor()) # use velocity to update position
