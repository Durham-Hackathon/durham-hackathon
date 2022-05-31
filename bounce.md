---
layout: default
---

[Previous step](/durham-hackathon/newton.html)

## How to bounce a ball

Next let's simulate what happens when we hit the floor. What we expect is that the ball (if it is perfectly elastic) will bounce back up. In a perfectly elastic collision no energy is lost, that's not entirely realistic but it is where we will start.

So the ball needs to change direction, or in other words, the velocity of the ball will change signs:

$$v \rightarrow -v$$

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
<textarea id="bounce-code" cols="40" rows="15" onkeydown="if(event.keyCode===9){var v=this.value,s=this.selectionStart,e=this.selectionEnd;this.value=v.substring(0, s)+'\t'+v.substring(e);this.selectionStart=this.selectionEnd=s+1;return false;}">
import turtle

# We will need the edges of our box, so we set them
# Note that the screen is centred on zero, so the edges are at:
# -width / 2 and width / 2
# and -height / 2 and height / 2
width = 300
height = 400
window = turtle.Screen()
window.setup(width, height)

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

# Free fall acceleration -g
g = -9.81

# Timestep size
t = 0.008

# Starting velocity
ux = 4
uy = 2

while True:
	#TODO: Bounce the ball by replacing break with your own code
    break;
</textarea><br /> 
<button type="button" onclick="runit()">Run</button> 
</form> 
<pre id="bounce-output" ></pre> 
<!-- If you want turtle graphics include a canvas -->
<div id="bounce-canvas"></div> 

</body> 

</html>

After you've got it bouncing off the floor introduce a ceiling and walls. The ball should bounce of the ceiling and the walls in the same way as it does off the floor. What do you need to change? What remains the same?

You will need to introduce a second velocity component. So now you have $$v_ux$$ and $$u_y$$ giving the x and y components of the velocity. To bounce off a ceiling or floor we modify the y component of the velocity, to bounce off of a wall we modify the x component.

Modify your while loop to include updates to the x-coordinate of the ball and the x velocity of the ball. Bear in mind that gravity does not act in the horizontal plane.

You will need to know the location of the floor as well. At the top you will see the size of the screen being set to `width` and `height`. Use these for your checks. The canvas is centered at 0. That means the floor will be at `-height/2` and the ceiling at `height/2`. The walls area analogously at `-width/2` and `width/2`.

To test these you need to modify the starting velocity which is currently set to 0 in x and y directions.

Fancy a hint? You can find the solution [here](code/step3-sol.py).

[Next step](/durham-hackathon/many-balls.html)


