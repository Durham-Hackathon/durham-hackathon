---
layout: default
---

##  How to derive the equations of motion?

Recall Newton's second law:

$$F=m\cdot a.$$

Can we use this to find out how the ball will move?

### Forces
What is $$F$$? This is the force acting on the ball. For now let's assume that is only gravity, so:

$$ F = m\cdot g,$$

where $$g \sim 9.81 \frac{m}{s^2}$$ is earth's gravitational constant.

Inserting this gives

$$m \cdot g = m \cdot a$$

or in other words

$$ g = a. $$


### Acceleration
What is $$a$$? This is the acceleration of our object. The acceleration depends on time, so we write $$a(t)$$ to denote the acceleration at time $$t$$.

We know that acceleration is just a change of velocity, so
$$ a(t) = \frac{d}{dt} v(t).$$
Similarily, we know that velocity is just a change in position, so
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

$$ g = a(t) = \frac{d}{dt} v(t) \sim \frac{v(t+h) - v(t)}{h}$$

This is equivalent to:

$$v(t+h) \sim v(t) + h \cdot g$$

So if we know the velocity and acceleration at time $$t$$ we can now compute it at a slightly later time. Rinse. Repeat.
This will give us the velocity at all future times.

The same thing works for the position of the ball:

$$v(t) = \frac{d}{dt} x(t) \sim \frac{x(t+h) - x(t)}{h}$$

And reforming:

$$x(t+h) \sim x(t) + h\cdot v(t).$$

Note that we need the velocity in order to compute the position.


