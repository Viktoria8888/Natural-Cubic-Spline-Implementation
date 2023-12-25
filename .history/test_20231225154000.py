import cv2
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import CubicSpline

# Load the image
image = cv2.imread('image.jpg', cv2.IMREAD_GRAYSCALE)

# Apply edge detection (you might need to adjust parameters)
edges = cv2.Canny(image, 50, 150)

# Find contours in the edges
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Extract points from the contours
points = []
for contour in contours:
    for point in contour:
        x, y = point[0]
        points.append((x, y))

# Sort the points based on x-coordinate
points = sorted(points, key=lambda p: p[0])

# Extract x and y coordinates
x_coordinates, y_coordinates = zip(*points)

# Create a cubic spline
cs = CubicSpline(x_coordinates, y_coordinates)

# Generate new x values for a smoother curve
new_x_values = np.linspace(min(x_coordinates), max(x_coordinates), 1000)

# Evaluate the cubic spline for the new x values
new_y_values = cs(new_x_values)

# Plot the original points and the cubic spline
plt.scatter(x_coordinates, y_coordinates, label='Original Points', color='red')
plt.plot(new_x_values, new_y_values, label='Cubic Spline', color='blue')
plt.title('Cubic Spline for Image Points')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.legend()
plt.show()
