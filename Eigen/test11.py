import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from mpl_toolkits.mplot3d import Axes3D

# -----------------------------
# Initial 3x3 matrix
# -----------------------------
A = np.array([[2, 1, 0],
              [1, 3, 1],
              [0, 1, 2]])

# -----------------------------
# Function to plot eigenvectors and transformation
# -----------------------------
def plot_eigen3D(A, ax):
    ax.clear()
    
    # Eigenvalues and eigenvectors
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    # Unit sphere
    phi, theta = np.mgrid[0:np.pi:30j, 0:2*np.pi:30j]
    x = np.sin(phi)*np.cos(theta)
    y = np.sin(phi)*np.sin(theta)
    z = np.cos(phi)
    ax.plot_wireframe(x, y, z, color='k', alpha=0.1, linewidth=0.5)
    
    # Transformed sphere
    points = np.vstack((x.flatten(), y.flatten(), z.flatten()))
    transformed_points = A @ points
    X_t = transformed_points[0].reshape(x.shape)
    Y_t = transformed_points[1].reshape(y.shape)
    Z_t = transformed_points[2].reshape(z.shape)
    ax.plot_wireframe(X_t, Y_t, Z_t, color='r', alpha=0.3)
    
    # Plot eigenvectors
    for i in range(3):
        vec = eigenvectors[:, i]
        ax.quiver(0, 0, 0, vec[0], vec[1], vec[2], color='b', length=1.0)
        ax.quiver(0, 0, 0, eigenvalues[i]*vec[0], eigenvalues[i]*vec[1], eigenvalues[i]*vec[2], color='g', length=1.0)
        ax.text(eigenvalues[i]*vec[0]*1.1, eigenvalues[i]*vec[1]*1.1, eigenvalues[i]*vec[2]*1.1,
                f'λ={eigenvalues[i]:.2f}', color='g')
    
    ax.set_xlim([-5,5])
    ax.set_ylim([-5,5])
    ax.set_zlim([-5,5])
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('3D Eigenvectors and Transformation of Unit Sphere')
    plt.draw()

# -----------------------------
# Plot setup
# -----------------------------
fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection='3d')
plt.subplots_adjust(left=0.25, bottom=0.35)  # leave space for sliders

plot_eigen3D(A, ax)

# -----------------------------
# Sliders for each matrix element
# -----------------------------
axcolor = 'lightgoldenrodyellow'
slider_axes = []
sliders = []
matrix_indices = [(i,j) for i in range(3) for j in range(3)]

for idx, (i,j) in enumerate(matrix_indices):
    ax_slider = plt.axes([0.25, 0.25-idx*0.025, 0.65, 0.02], facecolor=axcolor)
    slider = Slider(ax_slider, f'A[{i},{j}]', -5.0, 5.0, valinit=A[i,j])
    sliders.append(slider)

# -----------------------------
# Update function
# -----------------------------
def update(val):
    A_new = np.array([[s.val for s in sliders[0:3]],
                      [s.val for s in sliders[3:6]],
                      [s.val for s in sliders[6:9]]])
    plot_eigen3D(A_new, ax)

for s in sliders:
    s.on_changed(update)

plt.show()
