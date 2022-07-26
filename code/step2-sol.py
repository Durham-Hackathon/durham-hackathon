import turtle

width = 300
height = 400
window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

# Free fall acceleration
g = -9.81

# Timestep size
t = 0.08

# Starting velocity
u = 0 

while True:
    u += g*t  # update velocity in-place
    ball.sety(u*t + ball.ycor()) # use velocity to update position
    window.update()
