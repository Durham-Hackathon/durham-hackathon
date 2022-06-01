---
layout: default
---

[Previous step](/durham-hackathon/many-balls.html)

## How about different sizes of balls?

If we want balls of various sizes we need to consider which components of our simulation are affected by the mass of the ball. We know that (without friction) the weight does not affect the speed at which a ball falls. But what about the collisions? Here we have implicit assumption that the masses are the same. Why?

We have used *conservation of momentum*, momentum is mass times velocity, so in a collision between ball $$i$$ and ball $$j$$

$$m_i u_i = m_j u_j$$

And in the previous steps we have simply canceled out the masses. Now we need to put them back in.

<html> 
<head>
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script> 
<script src="js/skulpt.min.js" type="text/javascript"></script> 
<script src="js/skulpt-stdlib.js" type="text/javascript"></script> 
</head> 

<body> 
<script type="text/javascript"> 
function outf(text) { 
    var mypre = document.getElementById("bounce-output"); 
    mypre.innerHTML = mypre.innerHTML + text; 
} 
function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function runit() { 
   var prog = document.getElementById("bounce-code").value; 
   var mypre = document.getElementById("bounce-output"); 
   mypre.innerHTML = ''; 
   Sk.pre = "bounce-output";
   Sk.configure({output:outf, read:builtinRead}); 
   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'bounce-canvas';
   var myPromise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("<stdin>", false, prog, true);
   });
   myPromise.then(function(mod) {
       console.log('success');
   },
   function (err) {
  console.info('errorHandler', err);
  var msg = err.toString();
  }
   );
} 
</script> 

<h3>Add bounce:</h3> 
<form> 
<textarea id="bounce-code" cols="90" rows="15" onkeydown="if(event.keyCode===9){var v=this.value,s=this.selectionStart,e=this.selectionEnd;this.value=v.substring(0, s)+'\t'+v.substring(e);this.selectionStart=this.selectionEnd=s+1;return false;}">
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

        # Check for collisions, TODO: modify to account for the relative masses
        for j in range(N):
            if i != j and \
            abs(balls[i].xcor() - balls[j].xcor()) < 10 and \
            abs(balls[i].ycor() - balls[j].ycor()) < 10:
                        uxh = ux[i]
                        uyh = uy[i]
                        ux[i] = ux[j]
                        uy[i] = uy[j]
                        ux[j] = uxh
                        uy[j] = uyh

        window.update()


</textarea><br /> 
<button type="button" onclick="runit()">Run</button> 
</form> 
<pre id="bounce-output" ></pre> 
<!-- If you want turtle graphics include a canvas -->
<div id="bounce-canvas"></div> 

</body> 

</html>

Fancy a hint? You can find the solution [here](code/advanced1-sol.py).



