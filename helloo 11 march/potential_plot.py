import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the potential energy function
def potential(x, y):
    return (x**2 + y**2 - 0.25)**2
def potentialx(x, y):
    return 4*x*(x**2 + y**2 - 0.25)**2
def potentialy(x, y):
    return 4*y*(x**2 + y**2 - 0.25)**2

# Define the range of x and y values
x = np.linspace(-0.5, 0.5, 100)
y = np.linspace(-0.5, 0.5, 100)

# Create a grid of (x, y) values
X, Y = np.meshgrid(x, y)

# Calculate the potential energy values for each (x, y) pair
Z = potential(X, Y)
Zx = potentialx(X, Y)
Zy = potentialy(X, Y)

# Plot the potential energy surface
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Add the gradient vectors
ax.quiver(X, Y, Z, Zx, Zy, 0, length=0.1, normalize=True)

# Set labels and title
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Potential Energy')
ax.set_title('3D Surface of Potential Energy')

plt.show()





