import turtle
import random

# We will need the edges of our box, so we set them
width = 300
height = 400
window = turtle.Screen()
window.setup(width, height)
window.tracer(0)

color = ["blue",
        "yellow",
        "red",
        "darkgreen", 
        "cyan", 
        "violet",
        "magenta",
        "orange",
        "purple", 
        "navy", 
        "brown", 
        "maroon",
        "turquoise", 
        "lightgreen", 
        "green", 
        "skyblue", 
        "black", 
        "gold",
        "gray"]

N = 10 # Number of balls
balls = [] # A list to hold the balls
mass = []  # A list to hold masses of the balls

# Set up N balls and start them in random positions
for i in range(N):
    # Now the balls also have a mass
    mass.append(random.randint(1,4))

    balls.append(turtle.Turtle())
    balls[i].penup()
    balls[i].shape("circle")
    balls[i].shapesize(mass[i]**0.5)
    balls[i].color(color[i%len(color)])

    # Set random starting position
    balls[i].setx(random.randint(0,height / 4))
    balls[i].sety(random.randint(0,height / 4))

# Earth's gravitational constant
g = -9.81

# Timestep size
t = 0.008

# Starting velocity is now also a list, we need one velocity per ball
ux = []
uy = []
for i in range(N):
    ux.append(random.randint(-width/10,width/10))
    uy.append(0)

while True:
    for i in range(N):
        uy[i] += g*t
        balls[i].setx(ux[i]*t + balls[i].xcor())
        balls[i].sety(uy[i]*t + balls[i].ycor())

        if balls[i].ycor() < -height / 2 or balls[i].ycor() > height / 2:
            uy[i] = -uy[i]
        if balls[i].xcor() < -width / 2 or balls[i].xcor() > width / 2:
            ux[i] = -ux[i]

        # Check for collisions, now we need to modify
        for j in range(N):
            if i != j and \
            abs(balls[i].xcor() - balls[j].xcor()) < 10 and \
            abs(balls[i].ycor() - balls[j].ycor()) < 10:
                        uxh = ux[i]
                        uyh = uy[i]
                        ux[i] = mass[j]/mass[i] * ux[j]
                        uy[i] = mass[j]/mass[i] * uy[j]
                        ux[j] = mass[i]/mass[j] * uxh
                        uy[j] = mass[i]/mass[j] * uyh

        window.update()



