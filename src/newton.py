# Newton Method
# The Newton method is an iterative root-finding algorithm that uses the derivative of a function to find its roots. It works well if you have a good initial guess and the function is differentiable.

def function(x):
    return x**2 - 4*x + 3  # Example function x^2 - 4x + 3

def derivative(x):
    return 2*x - 4  # Derivative of the function: 2x - 4

def newton(initial_guess, tolerance=1e-7, max_iterations=1000):
    x = initial_guess
    for _ in range(max_iterations):
        f_x = function(x)
        df_x = derivative(x)
        
        # Avoid division by zero
        if df_x == 0:
            print("Derivative is zero. No solution found.")
            return None
        
        x_new = x - f_x / df_x
        
        # Check for convergence
        if abs(x_new - x) < tolerance:
            return x_new
        
        x = x_new
    
    print("Maximum iterations reached. No solution found.")
    return None

# Example usage
initial_guess1 = 0
initial_guess2 = 5
root1 = newton(initial_guess1)
root2 = newton(initial_guess2)

print("Real roots found using Newton method:")
if root1 is not None:
    print(root1)
if root2 is not None:
    print(root2)
