import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants (normalized units for simplicity)
G = 1
M = 1
c = 1

# Schwarzschild radius
R_s = 2 * G * M / c**2

# Simulation parameters
num_rays = 50000
disk_inner = 1.1 * R_s
disk_outer = 5 * R_s
max_distance = 8
rotation_speed = 0.02  # Disk rotation speed
spin = 0.5  # Kerr effect (simplified)

# Generate accretion disk rays
angles = np.random.uniform(0, 2*np.pi, num_rays)
radii = np.random.uniform(disk_inner, disk_outer, num_rays)
rays_x = radii * np.cos(angles)
rays_y = radii * np.sin(angles)

# Intensity profile: I(r) ~ r^-3/4
intensity = radii**(-0.75)
intensity /= intensity.max()  # Normalize

# Doppler shift and relativistic beaming
def doppler_colors(x, y, angular_velocity=0.5):
    vx = -angular_velocity * y
    vy = angular_velocity * x
    v_radial = (vx * x + vy * y) / (np.sqrt(x**2 + y**2) + 1e-6)
    # Relativistic beaming factor (simplified)
    beaming = (1 + v_radial)**3
    shift = np.clip(v_radial, -1, 1)
    r = np.clip((0.5 + 0.5 * shift) * beaming, 0, 1)
    g = 0.3 * beaming
    b = np.clip((0.5 - 0.5 * shift) * beaming, 0, 1)
    return np.stack([r, g, b], axis=1)

colors = doppler_colors(rays_x, rays_y) * intensity[:, None]

# Gravitational lensing with photon capture
def bend_ray(x, y, R_s, spin=0.5):
    distance = np.sqrt(x**2 + y**2)
    mask = distance > R_s  # Photon capture
    theta = np.arctan2(y, x)
    # Bending angle alpha = 4GM/(c^2 r)
    bend_factor = (4 * G * M / (c**2 * distance)) * (1 + spin * np.sin(theta))
    new_theta = theta + bend_factor
    new_x = np.where(mask, distance * np.cos(new_theta), np.nan)
    new_y = np.where(mask, distance * np.sin(new_theta), np.nan)
    return new_x, new_y

# Plot setup
fig, ax = plt.subplots(figsize=(8, 8))
scat = ax.scatter([], [], s=0.2, alpha=0.8)
ax.scatter(0, 0, color='black', s=700)  # Black hole
ax.set_xlim(-max_distance, max_distance)
ax.set_ylim(-max_distance, max_distance)
ax.axis('off')
ax.set_title("Scientific Black Hole Simulation")

# Animation update
def update(frame):
    # Rotate disk
    rotated_x = rays_x * np.cos(rotation_speed*frame) - rays_y * np.sin(rotation_speed*frame)
    rotated_y = rays_x * np.sin(rotation_speed*frame) + rays_y * np.cos(rotation_speed*frame)
    
    # Gravitational lensing
    bent_x, bent_y = bend_ray(rotated_x, rotated_y, R_s, spin)
    
    # Update Doppler colors
    updated_colors = doppler_colors(rotated_x, rotated_y) * intensity[:, None]
    
    scat.set_offsets(np.c_[bent_x, bent_y])
    scat.set_color(updated_colors)
    return scat,

ani = FuncAnimation(fig, update, frames=360, interval=30, blit=True)

plt.show()
