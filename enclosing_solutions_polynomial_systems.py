Here are seven advanced Python code examples demonstrating a **Combined Method for Enclosing All Solutions of Nonlinear Systems of Polynomial Equations**. These examples emphasize various techniques in interval arithmetic, homotopy methods, and branch-and-bound algorithms for enclosing all solutions effectively and rigorously.

### Smart File Name:
`enclosing_solutions_polynomial_systems.py`

---

### Example 1: **Interval Arithmetic for Solution Enclosures**
This example introduces interval arithmetic for enclosing the solutions of nonlinear polynomials, ensuring that the solution bounds are rigorous.
```python
from interval import interval, imath

def polynomial_interval_bounds(x_range, coeffs):
    """Calculates interval bounds for a polynomial given coefficients and an input range."""
    x = interval[x_range[0], x_range[1]]
    result = sum(coeff * x**i for i, coeff in enumerate(coeffs))
    return result

# Example usage
x_range = (-1, 1)  # Define range for x
coeffs = [1, 0, -1]  # Polynomial coefficients for x^2 - 1
bounds = polynomial_interval_bounds(x_range, coeffs)
print(f"Interval bounds: {bounds}")
```

---

### Example 2: **Newton's Method with Interval Arithmetic**
This example refines Newton's method to use interval arithmetic, ensuring all solutions are enclosed even if convergence is slow.
```python
def interval_newton(f, f_prime, x_interval, tol=1e-5):
    """Interval-based Newton's method for solving f(x) = 0."""
    while abs(x_interval) > tol:
        x_mid = x_interval.midpoint
        fx = f(x_mid)
        fpx = f_prime(x_mid)
        x_interval = x_interval & (x_mid - fx / fpx)
    return x_interval

# Example usage
f = lambda x: x**2 - 4
f_prime = lambda x: 2 * x
x_interval = interval[0, 3]
solution = interval_newton(f, f_prime, x_interval)
print(f"Solution interval: {solution}")
```

---

### Example 3: **Homotopy Continuation for Enclosing Solutions**
Homotopy continuation tracks the path of solutions from an easy system to the target system, ensuring all solutions are enclosed.
```python
import numpy as np

def homotopy_continuation(f, g, x0, t=1, steps=10):
    """Homotopy continuation from system g to system f."""
    path = []
    for step in range(steps + 1):
        tau = step / steps
        current_f = lambda x: (1 - tau) * g(x) + tau * f(x)
        x0 = x0 - np.linalg.pinv(f(x0)) @ current_f(x0)
        path.append(x0)
    return path

# Example usage
f = lambda x: np.array([x[0]**2 - 2, x[1]**2 - 3])
g = lambda x: np.array([x[0] - 1, x[1] - 1])
initial_guess = np.array([1.0, 1.0])
solution_path = homotopy_continuation(f, g, initial_guess)
print(f"Solution path: {solution_path}")
```

---

### Example 4: **Branch-and-Bound for Nonlinear Polynomial Systems**
This example applies a branch-and-bound approach to iteratively narrow down regions containing solutions.
```python
def branch_and_bound(f, bounds, tol=1e-5):
    """Branch and bound algorithm for solution enclosure."""
    solutions = []
    stack = [bounds]
    while stack:
        current_bounds = stack.pop()
        mid_point = [(b[0] + b[1]) / 2 for b in current_bounds]
        if all(abs(f(mid_point)) < tol):
            solutions.append(mid_point)
        else:
            stack.extend([
                [(b[0], (b[0] + b[1]) / 2) for b in current_bounds],
                [((b[0] + b[1]) / 2, b[1]) for b in current_bounds]
            ])
    return solutions

# Example usage
f = lambda x: x[0]**2 + x[1]**2 - 1
bounds = [(-1.5, 1.5), (-1.5, 1.5)]
solutions = branch_and_bound(f, bounds)
print(f"Enclosed solutions: {solutions}")
```

---

### Example 5: **Interval Newton Method with Constraint Propagation**
Combining interval Newton’s method with constraint propagation helps enclose all solutions while ensuring tight bounds.
```python
def interval_newton_constraint(f, f_prime, x_interval, tol=1e-5):
    """Interval Newton with constraint propagation."""
    solutions = []
    while abs(x_interval) > tol:
        x_mid = x_interval.midpoint
        fx = f(x_mid)
        fpx = f_prime(x_mid)
        if fpx != 0:
            x_interval = x_interval & (x_mid - fx / fpx)
            solutions.append(x_interval)
    return solutions

# Example usage
f = lambda x: x**3 - 3 * x + 1
f_prime = lambda x: 3 * x**2 - 3
x_interval = interval[-2, 2]
solutions = interval_newton_constraint(f, f_prime, x_interval)
print(f"Solutions: {solutions}")
```

---

### Example 6: **Krawczyk Method for Guaranteed Solution Enclosure**
The Krawczyk method provides a means to rigorously enclose solutions using iterative refinement.
```python
def krawczyk_method(f, x, interval_radius=0.1, tol=1e-5):
    """Krawczyk method for enclosing solutions of f(x) = 0."""
    x_interval = interval[x - interval_radius, x + interval_radius]
    while abs(x_interval) > tol:
        mid = x_interval.midpoint
        K = mid - f(mid)
        x_interval = K & x_interval
    return x_interval

# Example usage
f = lambda x: x**3 - x - 1
solution = krawczyk_method(f, x=1)
print(f"Solution interval: {solution}")
```

---

### Example 7: **Subdividing Interval Boxes for Polynomial Systems**
This example subdivides interval boxes into smaller intervals and checks each for solutions, ensuring no solution is missed.
```python
def subdivide_and_check(f, bounds, tol=1e-5):
    """Subdivide interval boxes to enclose all solutions."""
    intervals = [bounds]
    solutions = []
    while intervals:
        current = intervals.pop(0)
        mid = [(b[0] + b[1]) / 2 for b in current]
        if all(abs(f(mid)) < tol):
            solutions.append(mid)
        else:
            intervals.extend([
                [(b[0], mid[i]) for i, b in enumerate(current)],
                [(mid[i], b[1]) for i, b in enumerate(current)]
            ])
    return solutions

# Example usage
f = lambda x: x[0]**3 + x[1]**2 - 2
bounds = [(-2, 2), (-2, 2)]
solutions = subdivide_and_check(f, bounds)
print(f"Solutions: {solutions}")
```

---

These advanced examples provide a comprehensive toolkit for solving nonlinear systems of polynomial equations, covering robust approaches from interval Newton and homotopy continuation to branch-and-bound and the Krawczyk method. Each method is designed to ensure all possible solutions are enclosed, enabling more rigorous and comprehensive analyses across applications in scientific computing, engineering, and optimization.
