import turtle
import random

# We will need the edges of our box, so we set them
width = 400
height = 300
window = turtle.Screen()
window.setup(width+100, height+100)
window.tracer(10)

# Make sure program exits correctly
def on_close():
    global running
    running = False
window.getcanvas().winfo_toplevel().protocol("WM_DELETE_WINDOW", on_close)

# Draw window
t = turtle.Turtle()
t.penup()
t.setx(-width/2)
t.sety(-height/2)
t.pendown()
t.forward(width)
t.left(90)
t.forward(height)
t.left(90)
t.forward(width)
t.left(90)
t.forward(height)

Nx = 7 # Number of balls
Ny = 5 # Number of balls
balls = [] # A list to hold the balls

# Set up N balls and start them in random positions
for iy in range(Ny):
    for ix in range(Nx):
        idx = iy*Nx + ix
        balls.append(turtle.Turtle())
        balls[idx].penup()
        balls[idx].shape("circle")
        balls[idx].color("blue")

        # Set a grid of starting positions
        balls[idx].setx((ix+1)/(Nx+1)*width - width/2)
        # Only place in the upper half
        balls[idx].sety(iy/(Ny+1)*height/2 )

# Set up moving platform

class platform:
    def __init__(self):
        self.p = turtle.Turtle()
        self.p.shape("square")
        self.p.penup()
        self.p.shapesize(0.5,2)
        self.p.sety(-height/2 + 10)
        self.p.setx(0)
        self.sign = 0

    def xcor(self):
        return self.p.xcor()

    def ycor(self):
        return self.p.ycor()

    def left(self):
        if self.xcor() - 25 > -width/2:
            self.p.forward(-10)
            self.sign = -1

    def right(self):
        if self.xcor() + 25 < width/2:
            self.p.forward(10)
            self.sign = 1

platform = platform()
turtle.onkey(platform.left, "Left")
turtle.onkey(platform.right, "Right")
turtle.listen()

# Free fall acceleration
g = -9.81

# Timestep size
t = 0.008

# The moving ball
shot = turtle.Turtle()
shot.shape("circle")
shot.color("purple")
shot.penup()
shot.setx(0)
shot.sety(-50)
ux = 0    #velocity
uy = -100 #velocity

running = True
while running:
    uy += g*t
    shot.setx(shot.xcor() + ux*t)
    shot.sety(shot.ycor() + uy*t)

    # Check for bouncing off walls
    if shot.ycor() > height / 2:
        uy = -uy
        shot.sety(shot.ycor() - t*t*g)
    if shot.xcor() < -width / 2 or shot.xcor() > width / 2:
        ux = -ux

    # Check for collisions
    for ball in balls:
        if abs(shot.xcor() - ball.xcor()) < 10 and \
           abs(shot.ycor() - ball.ycor()) < 10:
                uy = -uy
                ball.ht()
                balls.remove(ball)

    # Check for collision with the platform
    if abs(shot.xcor() - platform.xcor()) < 15 and \
            shot.ycor() < platform.ycor() + 15:
            ux = platform.sign*10
            uy = -uy

    # Check for Game over
    if shot.ycor() < -height/2:
        # Game over
        turtle.delay(1000)
        ux, uy = 0, -100
        shot.setx(0)
        shot.sety(-50)
        platform.p.setx(0)

    window.update()

