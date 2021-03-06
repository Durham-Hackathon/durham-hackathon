import turtle

# We will need the edges of our box, so we set them
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
ux = 0.5
uy = 0

while True:
    uy += g*t  # update velocity in-place
    # no update needed for the x velocity since gravity only goes down
    ball.setx(ux*t + ball.xcor()) # use velocity to update position
    ball.sety(uy*t + ball.ycor()) # use velocity to update position

    if ball.ycor() < -height / 2 or ball.ycor() > height / 2:
        uy = -uy
        ball.sety(ball.ycor() - t*t*g)
    if ball.xcor() < -width / 2 or ball.xcor() > width / 2:
        ux = -ux
    window.update()
