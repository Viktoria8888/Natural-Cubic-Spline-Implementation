import matplotlib.pyplot as plt
import numpy as np

# Define some example polynomials
poly1 = np.poly1d([1, -2, 1])  # Example: (x - 1)^2
poly2 = np.poly1d([1, 0, -1])  # Example: x^2 - 1

# Create a range of x values
x_values = np.linspace(-2, 3, 100)

# Evaluate the polynomials at the x values
y_values_poly1 = poly1(x_values)
y_values_poly2 = poly2(x_values)

# Plotting
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))  # Create a 1x2 grid of subplots

# Plot the first polynomial
ax1.plot(x_values, y_values_poly1, label='(x - 1)^2')
ax1.set_title('Polynomial 1')
ax1.legend()

# Plot the second polynomial
ax2.plot(x_values, y_values_poly2, label='x^2 - 1')
ax2.set_title('Polynomial 2')
ax2.legend()

plt.show()
