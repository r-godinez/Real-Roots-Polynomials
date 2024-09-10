function root = bisection(a, b, tol)
    % Define the function
    f = @(x) x^3 + x + 1; % The function f(x) = x^3 + x + 1

    % Check if the initial guesses are valid
    if f(a) * f(b) >= 0
        error('Function must have different signs at a and b')
    end

    % Bisection method loop
    while (b - a) / 2 > tol
        midpoint = (a + b) / 2;
        
        if f(midpoint) == 0  % Exact root found
            root = midpoint;
            return;
        elseif f(a) * f(midpoint) < 0
            b = midpoint;
        else
            a = midpoint;
        end
    end

    % Return the root
    root = (a + b) / 2;
end

% Example usage:
root1 = bisection(-1, 0, 1e-7);  % Root between -1 and 0

fprintf('Real root found:\n');
fprintf('Root 1: %.7f\n', root1);
