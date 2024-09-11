// Function definition: f(x) = x^3 + x + 1
function f(x) {
    return Math.pow(x, 3) + x + 1;
}

// Derivative of f(x): f'(x) = 3x^2 + 1
function derivative(x) {
    return 3 * Math.pow(x, 2) + 1;
}

// Newton's method implementation
function newtonMethod(initialGuess, tolerance = 1e-7, maxIterations = 1000) {
    let x = initialGuess;  // Start with the initial guess

    // Iterate for a maximum number of iterations
    for (let i = 0; i < maxIterations; i++) {
        let f_x = f(x);  // Function value at x
        let df_x = derivative(x);  // Derivative value at x

        // Avoid division by zero
        if (df_x === 0) {
            console.log("Derivative is zero. No solution found.");
            return null;
        }

        // Newton's method formula: x_new = x - f(x) / f'(x)
        let x_new = x - f_x / df_x;

        // Check if the difference between consecutive guesses is within the tolerance
        if (Math.abs(x_new - x) < tolerance) {
            return x_new;
        }

        // Update x for the next iteration
        x = x_new;
    }

    console.log("Maximum iterations reached. No solution found.");
    return null;  // No root found
}

// Example usage
let initialGuess = 0;  // Initial guess for the root
let tolerance = 1e-7;  // Tolerance for convergence
let maxIterations = 1000;  // Maximum number of iterations

let root = newtonMethod(initialGuess, tolerance, maxIterations);  // Find the root

// Output the found root, if any
if (root !== null) {
    console.log("Root found: " + root);
} else {
    console.log("No root found.");
}
