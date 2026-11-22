import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Define the grid
x = np.linspace(-5, 5, 20)
y = np.linspace(-5, 5, 20)
X, Y = np.meshgrid(x, y)

# Gravitational field calculation
def gravitational_field(X, Y, mass_x, mass_y):
    dx = X - mass_x
    dy = Y - mass_y
    r = np.sqrt(dx**2 + dy**2)  # Distance to the mass
    r = np.maximum(r, 0.5)  # Clamp minimum distance to avoid singularities
    
    # Compute the field with a more gradual change
    Fx = -dx / r**2
    Fy = -dy / r**2
    magnitude = np.sqrt(Fx**2 + Fy**2)  # Calculate the magnitude of the field
    
    # Normalize the field to scale it gradually for visualization
    magnitude = magnitude / (0.01 + magnitude)  # Smooth scaling
    Fx *= magnitude
    Fy *= magnitude
    return Fx, Fy, magnitude

# Set up the plot
plt.figure(figsize=(6, 6))
plt.xlim(-5, 5)
plt.ylim(-5, 5)
plt.gca().set_aspect('equal', adjustable='box')
plt.title("Gravitational Vector Field (Single Moving Mass)")
plt.xlabel("x")
plt.ylabel("y")

# Initialize the mass position and field
mass_x, mass_y = 2, 0  # Starting position
Fx, Fy, magnitude = gravitational_field(X, Y, mass_x, mass_y)

# Draw the initial mass and field vectors
mass_marker, = plt.plot([mass_x], [mass_y], 'ro', markersize=12, label="Mass (M)")
quiver = plt.quiver(X, Y, Fx, Fy, magnitude, cmap="plasma", scale=15, width=0.003)

# Animation function
def update(frame):
    global mass_x, mass_y
    # Circular motion of the mass
    angle = frame * np.pi / 15
    mass_x = np.cos(angle) * 2
    mass_y = np.sin(angle) * 2
    
    # Recalculate the field
    Fx, Fy, magnitude = gravitational_field(X, Y, mass_x, mass_y)
    
    # Update mass position and field vectors
    mass_marker.set_data([mass_x], [mass_y])  # Wrap in lists
    quiver.set_UVC(Fx, Fy, magnitude)  # Update vector directions and sizes
    return mass_marker, quiver

# Create animation
ani = FuncAnimation(plt.gcf(), update, frames=60, interval=100, blit=False)

plt.colorbar(quiver, label="Gravitational Field Magnitude")
plt.legend()
plt.show()
ani.save('gravitational_field_animation.mp4', writer='ffmpeg', fps=12)
