---
layout: default
---

[Previous step](/durham-hackathon/first-steps.html)


## A first simulation: What happens when we drop an elastic ball?

Recall Newton's first law:

$$F=m\cdot a.$$

Can we use this to find out how the ball will move?

### Forces
What is $$F$$? This is the force acting on the ball. For now let's assume that is only gravity, so:

$$ F = m\cdot g,$$

where $$g \sim 9.81 \frac{m}{s^2}$$ is earth's gravitational constant.

Inserting this gives

$$g\cdot m = m \cdot a$$

or in other words

$$ g = a. $$


### Acceleration
What is $$a$$? This is the acceleration of our object. The acceleration depends on time, so we write $$a(t)$$ to denote the acceleration at time $$t$$.

We know that acceleration is just a change of velocity, so
$$ a(t) = \frac{d}{dt} v(t).$$
Similarily, we know that velocity is just a change in velocity, so
$$v(t) = \frac{d}{dt} x(t).$$

This type of equation, in which we need to solve for a derivative is called an ordinary differential equation (ODE).
They are extremely common throughout physics and engineering and solving them quickly is very useful.

Sometimes (such as here) an ODE can be solved by hand, but in many other cases that is not possible.
In these cases we can try to find the solution approximately using a numerical simulation.

The derivative is defined as:

$$\frac{d}{dt} f(t) =\lim_{h->0} \frac{f(t+h) - f(t)}{h}$$

So we should let $h$ tend to zero, but what happens if we just choose a small h instead?

We get an approximation of the true derivative that we can easily calculate, after all we know all the quantities on the right side of the equation.

There is a lot of mathematical theory concerned with how big we can safely choose $$h$$ (stability) and what size of error we are making (convergence).
We will ignore all this for now and go back to our two equations and insert this approximation:

$$ g = a(t) = \frac{d}{dt} v(t) \sim \frac{v(t+h) + v(t)}{h}$$

This is equivalent to:

$$v(t+h) \sim v(t) + h \cdot g$$

So if we know the velocity and acceleration at time $$t$$ we can now compute it at a slightly later time. Rinse. Repeat.
This will give us the velocity at all future times.

The same thing works for the position of the ball:

$$v(t) = \frac{d}{dt} x(t) \sim \frac{x(t+h) - x(t)}{h}$$

And reforming:

$$x(t+h) \sim x(t) + h\cdot v(t).$$

Note that we need the velocity in order to compute the position.

Now let's rewrite the code for the falling ball from above with correct physics:

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

The solution can be found [here](https://github.com/Durham-Hackathon/durham-hackathon/code/step2-sol.py)

[Next step](/durham-hackathon/bounce.html)
