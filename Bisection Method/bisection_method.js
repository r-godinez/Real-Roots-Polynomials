// Function definition: f(x) = x^3 + x + 1
function f(x) {
    return Math.pow(x, 3) + x + 1;
}

// Bisection method implementation
function bisectionMethod(a, b, tolerance = 1e-7, maxIterations = 1000) {
    // Ensure the initial interval [a, b] has a sign change
    if (f(a) * f(b) >= 0) {
        console.log("Bisection method requires that the function changes sign over the interval.");
        return null; // No root found
    }

    let mid; // Midpoint of the interval

    // Iterate until convergence or max iterations reached
    for (let i = 0; i < maxIterations; i++) {
        mid = (a + b) / 2; // Midpoint
        let f_mid = f(mid); // Function value at the midpoint

        // If the function value at the midpoint is within the tolerance, return the midpoint as the root
        if (Math.abs(f_mid) < tolerance) {
            return mid;
        }

        // Determine which subinterval to use for the next iteration
        if (f(a) * f_mid < 0) {
            b = mid; // Root is in the left subinterval [a, mid]
        } else {
            a = mid; // Root is in the right subinterval [mid, b]
        }
    }

    console.log("Maximum iterations reached. No solution found.");
    return null; // No root found
}

// Example usage
let a = -1;  // Start of the interval
let b = 0;   // End of the interval
let tolerance = 1e-7;  // Tolerance for convergence
let maxIterations = 1000; // Maximum number of iterations

let root = bisectionMethod(a, b, tolerance, maxIterations); // Find the root

// Output the found root, if any
if (root !== null) {
    console.log("Root found: " + root);
} else {
    console.log("No root found.");
}
