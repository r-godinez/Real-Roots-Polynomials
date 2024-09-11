% Function definition: f(x) = x^3 + x + 1
f = @(x) x.^3 + x + 1;

% Parameters
num_segments = 20;  % Number of segments
a = -1;             % Start of the interval
b = 0;              % End of the interval

% Create x values
x_values = linspace(a, b, num_segments + 1);
y_values = f(x_values);

% Plot the curve
figure;
hold on;
axis([a b min(y_values) max(y_values)]);
grid on;

% Plot line segments
for i = 1:num_segments
    x1 = x_values(i);
    x2 = x_values(i + 1);
    y1 = f(x1);
    y2 = f(x2);
    
    % Plot line segment
    plot([x1, x2], [y1, y2], 'k-', 'LineWidth', 1);
end

% Add labels and title
xlabel('x');
ylabel('f(x)');
title('Plot of f(x) = x^3 + x + 1 using Short Line Segments');
hold off;
