# Bisection Method
# The Bisection method is a robust numerical technique for finding roots.
# It works by repeatedly bisecting an interval [a, b] and selecting a subinterval in which a root must lie.
# This method requires that the function changes sign over the interval [a, b] (i.e., f(a) * f(b) < 0).

def function(x):
    return x**3 + x + 1  # Defines the function f(x) = x^3 + x + 1 for which we want to find the root

def bisection_method(a, b, tolerance=1e-7, max_iterations=1000):
    """
    Function to find a real root of a function using the Bisection Method.
    
    Parameters:
    a (float): The lower bound of the interval where a root is expected
    b (float): The upper bound of the interval where a root is expected
    tolerance (float): The acceptable error margin for the root (default: 1e-7)
    max_iterations (int): The maximum number of iterations to run (default: 1000)
    
    Returns:
    float: The approximate root of the function within the tolerance level
    """
    
    # Check if the function has opposite signs at a and b
    # This is a necessary condition for the Bisection Method to work
    if function(a) * function(b) >= 0:
        print("Bisection method requires that the function changes sign over the interval.")
        return None
    
    # Perform iterations to progressively narrow down the interval
    for _ in range(max_iterations):
        # Calculate the midpoint of the interval [a, b]
        c = (a + b) / 2
        
        # Evaluate the function at the midpoint
        f_c = function(c)
        
        # Check if the midpoint is a good approximation of the root
        # If the absolute value of f(c) is less than the tolerance, we assume it's close enough to the root
        if abs(f_c) < tolerance:
            return c  # Return the midpoint as the root
        
        # Decide which subinterval to keep for the next iteration
        # If f(a) and f(c) have opposite signs, the root lies between a and c
        if function(a) * f_c < 0:
            b = c  # Update b to the midpoint c
        else:
            a = c  # Otherwise, update a to the midpoint c
    
    # If the loop completes without finding a root, we return a message and None
    print("Maximum iterations reached. No solution found.")
    return None

# Example usage of the Bisection Method
a = -1  # Lower bound of the interval
b = 0   # Upper bound of the interval

# Call the bisection_method function to find the root
r1 = bisection_method(a, b)

# Output the result
print("Real roots found using Bisection method:")
if r1 is not None:
    print(r1)  # Print the root if it was found
