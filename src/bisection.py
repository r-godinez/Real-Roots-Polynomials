# Bisection Method
# The Bisection method is a robust numerical technique for finding roots and does not require the derivative of the function. It works by repeatedly bisecting an interval and selecting a subinterval in which a root must lie.

def function(x):
    return x**2 - 4*x + 3  # Example function x^2 - 4x + 3

def bisection_method(a, b, tolerance=1e-7, max_iterations=1000):
    if function(a) * function(b) >= 0:
        print("Bisection method requires that the function changes sign over the interval.")
        return None
    
    for _ in range(max_iterations):
        c = (a + b) / 2
        f_c = function(c)
        
        if abs(f_c) < tolerance:
            return c
        
        if function(a) * f_c < 0:
            b = c
        else:
            a = c
    
    print("Maximum iterations reached. No solution found.")
    return None

# Example usage
a = 0
b = 2
root1 = bisection_method(a, b)

a = 2
b = 5
root2 = bisection_method(a, b)

print("Real roots found using Bisection method:")
if root1 is not None:
    print(root1)
if root2 is not None:
    print(root2)
