---
layout: default
---

##  What happens when we drop an elastic ball?

Imagine a ball of mass $$m$$ and the goal to simulate and visualize its free fall with Python.

The Python code below uses the graphics library turtle to draw a `ball`.
`ball` is a turtle object and can be configured with the help of the `color()` and `shape()` methods.
Further, our `ball` object has got a method `ball.ycor()` that returns its current position along the $$y$$-axis, which we imagine as the balls height above the floor. 
Other from that, the code contains an infinite loop `while True:` that is used to draw our `ball` over and over again.

Let's give it a try and drop our digital ball! In the infinite loop, try to modify the position of the `ball` so it begins to fall:
1. Use `ball.sety(val)` to set the $$y$$-position of `ball` to a value `val`
2. Use `ball.ycor()` to get the current $$y$$-position of `ball`
3. Combine both steps to animate the `ball`
4. What happens if you experiment with different values `val`?
5. How close is your animation to reality?

<html> 
<head> 
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script> 
<script src="js/skulpt.min.js" type="text/javascript"></script> 
<script src="js/skulpt-stdlib.js" type="text/javascript"></script> 

</head> 

<body> 

<script type="text/javascript"> 

function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function runit() {
   var prog = document.getElementById("firststeps").value; 
   Sk.configure({read:builtinRead}); 
   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'first-canvas';
   var myPromise = Sk.misceval.asyncToPromise(function() {
       return Sk.importMainWithBody("<stdin>", false, prog, true);
   });
   myPromise.then(function(mod) {
       console.log('success');
   },
       function(err) {
       console.log(err.toString());
   });
}
</script> 

<h3>First Steps:</h3> 
<form> 
<textarea id="firststeps" cols="60" rows="12" onkeydown="if(event.keyCode===9){var v=this.value,s=this.selectionStart,e=this.selectionEnd;this.value=v.substring(0, s)+'\t'+v.substring(e);this.selectionStart=this.selectionEnd=s+1;return false;}">
import turtle

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

while True:
    #TODO: Drop the ball by inserting your code below
</textarea><br /> 
<button type="button" onclick="runit()">Run</button> 
</form>

<div id="first-canvas"></div> 

</body> 

</html> 
Fancy a hint? You can find the solution [here](https://github.com/Durham-Hackathon/durham-hackathon/code/step1-sol.py).
<!--Fancy a hint? You can find the solution [here](code/step1-sol.py).-->

Since we are arbitrarily fantasising the speed of the ball, this is indeed not a physical *simulation* but just an *animation*. Let's try to figure out how the ball should actually move!

[Next step](/durham-hackathon/newton.html)

