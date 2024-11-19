Simulates Hamiltonian flow on the Torus  (as $ℝ^2/{ℤ^2}$) by plotting random points on the torus and flowing them.
Using [matplotlib](https://matplotlib.org/) in python.

NOTE - this is not completely accurate due to many factors, like the discretization of time, or the inaccuracies of calculating sin/cos. This inaccuracy can be (somewhat) gauged by seeing H applied to an orbit of a point change.

Here is the example $H(p,q) = \sin(2\pi p) +\cos(2\pi q)$.

![](demo.gif)
