# Newton Method
# The Newton method (also known as Newton-Raphson method) is an iterative algorithm used to find the root of a function.
# It requires both the function and its derivative, and works well with a good initial guess.

def function(x):
    """
    Defines the function for which we want to find the root.
    
    Parameters:
    x (float): The input value for the function.
    
    Returns:
    float: The value of f(x) = x^3 + x + 1 at the given x.
    """
    return x**3 + x + 1  # This is the function f(x) = x^3 + x + 1

def derivative(x):
    """
    Defines the derivative of the function f(x).
    
    Parameters:
    x (float): The input value for the derivative.
    
    Returns:
    float: The value of f'(x) = 3x^2 + 1 at the given x.
    """
    return 3*x**2 + 1  # This is the derivative f'(x) = 3x^2 + 1

def newton(initial_guess, tolerance=1e-7, max_iterations=1000):
    """
    Implements Newton's method for finding the root of a function.
    
    Parameters:
    initial_guess (float): The starting point for Newton's method.
    tolerance (float): The acceptable error margin for convergence. The algorithm stops when the result is within this tolerance (default: 1e-7).
    max_iterations (int): The maximum number of iterations before the algorithm stops if it doesn't converge (default: 1000).
    
    Returns:
    float: The approximate root of the function if found within tolerance, otherwise None.
    """
    
    # Initialize x to the initial guess provided by the user
    x = initial_guess
    
    # Loop over a maximum of 'max_iterations' times to find the root
    for _ in range(max_iterations):
        f_x = function(x)  # Calculate the value of the function at the current x
        df_x = derivative(x)  # Calculate the value of the derivative at the current x
        
        # Check if the derivative is zero to avoid division by zero (undefined behavior)
        if df_x == 0:
            print("Derivative is zero. No solution found.")  # Print error message if the derivative is zero
            return None  # Return None to indicate failure
        
        # Apply the Newton-Raphson update formula: x_new = x - f(x) / f'(x)
        x_new = x - f_x / df_x
        
        # Check if the absolute difference between the new and old x values is within the tolerance
        if abs(x_new - x) < tolerance:
            return x_new  # If the difference is small enough, return the new value as the root
        
        # Update x to the new value for the next iteration
        x = x_new
    
    # If the maximum number of iterations is reached without convergence, print a message
    print("Maximum iterations reached. No solution found.")
    return None  # Return None if the root is not found within the given iterations

# Example usage of the Newton method to find a root
initial_guess1 = -1  # Set an initial guess for the root
r1 = newton(initial_guess1)  # Call the newton function with the initial guess

# Print the result
print("Real roots found using Newton method:")
if r1 is not None:
    print(r1)  # If a root is found, print it
