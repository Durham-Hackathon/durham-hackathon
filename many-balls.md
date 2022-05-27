---
layout: default
---

[Previous step](/durham-hackathon/bounce.html)

## Improving the simulation: Can we add more balls?

Of course we can. We only need an extra loop that runs over all the balls.


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

width = 300
height = 400
window = turtle.Screen()
window.setup(width, height)

gravity = -9.81
h = 0.08
vx = 0 # Starting velocity in x direction
vy = 0 # Starting velocity in y direction

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

while True:
    # Add your code here
    vy = vy + h*gravity
    y = ball.ycor() + h*vy
    ball.sety(y)
</textarea><br /> 
<button type="button" onclick="runit()">Run</button> 
</form> 
<pre id="bounce-output" ></pre> 
<!-- If you want turtle graphics include a canvas -->
<div id="bounce-canvas"></div> 

</body> 

</html>


At this point you can either move on to the more advanced topics listed in the index or you can customise your simulation.

The easiest thing to start with is changing the colors. Pick your own in the list. The list is not exhaustive, there are other colors you could add. Or you can change the order of the list, with a few balls only the first colors are used.

The next thing is to change the shape of the ball. Perhaps you would prefer to show squares? Or turtles?
- Options: `arrow`, `turtle`, `circle`, `square`, `triangle`, `classic`
- You can also make your own shape by passing in nodes of a polygon:
    ``s = Shape("compound")
      poly1 = ((0,0),(10,-5),(0,10),(-10,-5))
      s.addcomponent(poly1, "red", "blue")
      poly2 = ((0,0),(10,-5),(-10,-5))
      s.addcomponent(poly2, "blue", "red")``
  Then register your new shape `register_shape("myshape", s)` and set it using `ball.shape("myshape")` as before.

You can even change the background color by setting the background color
``window.bgcolor("orange")``

For the documentation explaining all the options the turtle library provides look [here](https://docs.python.org/3/library/turtle.html#). Like many python projects, turtle is well-documented.


Fancy a hint? You can find the solution [here](code/step4-sol.py).



