// Function definition: f(x) = x^3 + x + 1
function f(x) {
    return Math.pow(x, 3) + x + 1;
}

// Parameters
const numSegments = 20;  // Number of segments
const a = -1;            // Start of the interval
const b = 0;             // End of the interval
const width = 80;        // Width of the plot area
const height = 20;       // Height of the plot area

// Create an empty plot
let plot = Array.from({ length: height }, () => Array(width).fill(' '));

// Calculate function values and min/max
const step = (b - a) / numSegments;
const xValues = Array.from({ length: numSegments + 1 }, (_, i) => a + i * step);
const yValues = xValues.map(x => f(x));
const minY = Math.min(...yValues);
const maxY = Math.max(...yValues);

// Map function value to plot area height
function mapToHeight(y) {
    return Math.round((y - minY) / (maxY - minY) * (height - 1));
}

// Draw the line segments
for (let i = 0; i < numSegments; i++) {
    const x1 = xValues[i];
    const x2 = xValues[i + 1];
    const y1 = f(x1);
    const y2 = f(x2);

    const x1Plot = Math.round((x1 - a) / (b - a) * (width - 1));
    const x2Plot = Math.round((x2 - a) / (b - a) * (width - 1));
    const y1Plot = mapToHeight(y1);
    const y2Plot = mapToHeight(y2);

    if (x1Plot !== x2Plot) {
        const xStart = Math.min(x1Plot, x2Plot);
        const xEnd = Math.max(x1Plot, x2Plot);

        for (let x = xStart; x <= xEnd; x++) {
            const yPlot = y1Plot + (y2Plot - y1Plot) * (x - x1Plot) / (x2Plot - x1Plot);
            if (yPlot >= 0 && yPlot < height) {
                plot[height - 1 - Math.round(yPlot)][x] = '*';
            }
        }
    }
}

// Print the plot
plot.forEach(row => console.log(row.join('')));
