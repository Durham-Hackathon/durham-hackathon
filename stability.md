---
layout: default
---

##  Analysing the method

There is a difference between a numerical simulation and reality. As you have already seen part of this is due to the model. There are always more physical effects to add. Most models are simplifications. But even if our model were perfect we still wouldn't get a perfect simulation. Why is that?

There are at least two more problems. The first is that our calculation in the computer is not exact. Computers use floating point arithmetic, which you can read up on [here](https://en.wikipedia.org/wiki/Floating-point_arithmetic). So each calculation we make introduces a miniscule error.

The second is that we haven't actually computed the derivatives in time from our equation, we approximate them! And this introduces an error too. This error will get smaller if we reduce the timestep size $$t$$. The smaller we take it the closer our approximation is to the true derivative.

But sometimes the error get's very large, in these cases we say that our approximation is not **stable**. The smallest timestep which produces a stable approximation (e.g. one with a small error) can be calculated. It depends effectively on the speed at which things change. So, for updating the position it is the velocity $$u$$ and for updating the velocity it is the gravitational constant $$g$$.

At this point you need quite a lot of [math](https://en.wikipedia.org/wiki/Euler_method#Numerical_stability) to really understand what is going on. But essentially the timestep size $$t$$ must always be smaller than $$2/c$$ where $$c$$ is the absolute value of the speed at which the variable we are looking at is changing. In our case we need to take the more restrictive of the two conditions.


