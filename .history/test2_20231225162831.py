import matplotlib.pyplot as plt
import numpy as np

# Generate some data for the graphs
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = x**2

# Plot the first graph
plt.plot(x, y1, label='sin(x)')

# Plot the second graph
plt.plot(x, y2, label='cos(x)')

# Plot the third graph
plt.plot(x, y3, label='x^2')

# Add labels and legend
plt.xlabel('x-axis')
plt.ylabel('y-axis')
plt.legend()

# Show the plot
plt.show()
