#include <stdio.h>
#include <math.h>

#define WIDTH 80  // Width of the plot area
#define HEIGHT 20 // Height of the plot area

// Function definition: f(x) = x^3 + x + 1
double f(double x) {
    return pow(x, 3) + x + 1;
}

// Map function value to plot area height
int mapToHeight(double y, double minY, double maxY) {
    return (int)((y - minY) / (maxY - minY) * (HEIGHT - 1));
}

int main() {
    int num_segments = 20;  // Number of segments
    double a = -1;          // Start of the interval
    double b = 0;           // End of the interval
    double step = (b - a) / num_segments;  // Step size for the interval

    // Calculate min and max of function values for scaling
    double minY = f(a);
    double maxY = f(a);

    for (int i = 1; i <= num_segments; i++) {
        double x = a + i * step;   // Calculate x value
        double y = f(x);          // Calculate function value

        if (y < minY) minY = y;
        if (y > maxY) maxY = y;
    }

    // Create the plot area
    char plot[HEIGHT][WIDTH];
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            plot[i][j] = ' ';
        }
    }

    // Draw the line segments
    for (int i = 0; i < num_segments; i++) {
        double x1 = a + i * step;
        double x2 = a + (i + 1) * step;
        double y1 = f(x1);
        double y2 = f(x2);

        int x1_plot = (int)((x1 - a) / (b - a) * (WIDTH - 1));
        int x2_plot = (int)((x2 - a) / (b - a) * (WIDTH - 1));
        int y1_plot = mapToHeight(y1, minY, maxY);
        int y2_plot = mapToHeight(y2, minY, maxY);

        if (x1_plot != x2_plot) {
            int x_start = x1_plot < x2_plot ? x1_plot : x2_plot;
            int x_end = x1_plot > x2_plot ? x1_plot : x2_plot;

            for (int x = x_start; x <= x_end; x++) {
                int y_plot = y1_plot + (y2_plot - y1_plot) * (x - x1_plot) / (x2_plot - x1_plot);
                if (y_plot >= 0 && y_plot < HEIGHT) {
                    plot[HEIGHT - 1 - y_plot][x] = '*';
                }
            }
        }
    }

    // Print the plot
    for (int i = 0; i < HEIGHT; i++) {
        for (int j = 0; j < WIDTH; j++) {
            printf("%c", plot[i][j]);
        }
        printf("\n");
    }

    return 0;
}
