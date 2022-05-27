---
layout: default
---

[Previous step](/durham-hackathon/first-steps.html)


## How to drop a ball *for real*

The *equations of motion* are a set of formulas that enable us to describe the movement of an object. An object in free fall simply moves along a straight line since it is only driven by earth's gravitational force that accelerates the object by means of the  earth's gravitational constant $$g \sim 9.81 \frac{m}{s^2}$$. Therefore, we only need to consider the equations of motion for linear motion with constant acceleration.

To describe the motion of an object, we consider the following values:
- the initial velocity $$u$$ 
- the constant acceleration $$a$$, in our case, $$a = g$$
- a time $$t$$, meaning, the duration of the motion
- a distance $$x$$, meaning, how far the object moves

Based thereon, we can compute the distance $$s$$ that an object travels in a certain amount of time $$t$$ as follows:
$$x = v \cdot t$$

As you can see, this requires us to know the velocity $$v$$ of the object. For linear motions with constant accleration, $$v$$ can be computed as follows:
$$v = u + a \cdot t$$

Or, in the case of free fall:
$$v = u + g \cdot t$$

Now let's rewrite the code for the falling ball from the previous step with correct physics:

<html> 
<head> 
<script src="https://ajax.googleapis.com/ajax/libs/jquery/1.9.0/jquery.min.js" type="text/javascript"></script> 
<script src="js/skulpt.min.js" type="text/javascript"></script> 
<script src="js/skulpt-stdlib.js" type="text/javascript"></script> 
</head> 

<body> 

<script type="text/javascript"> 
function outf(text) { 
    var mypre = document.getElementById("newton-output"); 
    mypre.innerHTML = mypre.innerHTML + text; 
} 
function builtinRead(x) {
    if (Sk.builtinFiles === undefined || Sk.builtinFiles["files"][x] === undefined)
            throw "File not found: '" + x + "'";
    return Sk.builtinFiles["files"][x];
}

function runit() { 
   var prog = document.getElementById("newton-code").value; 
   var mypre = document.getElementById("newton-output"); 
   mypre.innerHTML = ''; 
   Sk.pre = "newton-output";
   Sk.configure({output:outf, read:builtinRead}); 
   (Sk.TurtleGraphics || (Sk.TurtleGraphics = {})).target = 'newton-canvas';
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

<h3>Add gravity:</h3> 
<form> 
<textarea id="newton-code" cols="40" rows="15" onkeydown="if(event.keyCode===9){var v=this.value,s=this.selectionStart,e=this.selectionEnd;this.value=v.substring(0, s)+'\t'+v.substring(e);this.selectionStart=this.selectionEnd=s+1;return false;}">
import turtle

gravity = 9.81
h = 0.008
v = 0 # Starting velocity

ball = turtle.Turtle()
ball.penup()
ball.color("red")
ball.shape("circle")

while True:
    # Add your code here
</textarea><br /> 
<button type="button" onclick="runit()">Run</button> 
</form> 
<pre id="newton-output" ></pre> 
<!-- If you want turtle graphics include a canvas -->
<div id="newton-canvas"></div> 

</body> 

</html>

Fancy a hint? You can find the solution [here](code/step2-sol.py).

Want to know where all these equations actually come frome? Take a look [here](/durham-hackathon/motion-equations.html)

[Next step](/durham-hackathon/bounce.html)
