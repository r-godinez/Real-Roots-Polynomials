import numpy as np

# Function definition: f(x) = x^3 + x + 1
def f(x):
    return x**3 + x + 1

# Parameters
num_segments = 20  # Number of segments
a = -1             # Start of the interval
b = 0              # End of the interval
width = 80         # Width of the plot area
height = 20        # Height of the plot area

# Calculate step size
step = (b - a) / num_segments

# Create an empty plot
plot = [[' ' for _ in range(width)] for _ in range(height)]

# Calculate min and max values of the function for scaling
x_values = np.linspace(a, b, num_segments + 1)
y_values = [f(x) for x in x_values]
min_y = min(y_values)
max_y = max(y_values)

# Map function value to plot area height
def map_to_height(y, min_y, max_y):
    return int((y - min_y) / (max_y - min_y) * (height - 1))

# Draw the line segments
for i in range(num_segments):
    x1 = a + i * step
    x2 = a + (i + 1) * step
    y1 = f(x1)
    y2 = f(x2)

    x1_plot = int((x1 - a) / (b - a) * (width - 1))
    x2_plot = int((x2 - a) / (b - a) * (width - 1))
    y1_plot = map_to_height(y1, min_y, max_y)
    y2_plot = map_to_height(y2, min_y, max_y)

    if x1_plot != x2_plot:
        for x in range(min(x1_plot, x2_plot), max(x1_plot, x2_plot) + 1):
            y_plot = y1_plot + (y2_plot - y1_plot) * (x - x1_plot) / (x2_plot - x1_plot)
            if 0 <= y_plot < height:
                plot[height - 1 - int(y_plot)][x] = '*'

# Print the plot
for row in plot:
    print(''.join(row))
