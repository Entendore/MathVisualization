import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# -----------------------------
# Initial matrix
# -----------------------------
A = np.array([[3, 1],
              [1, 2]])

# -----------------------------
# Function to compute eigenvectors and plot
# -----------------------------
def plot_eigen(A):
    eigenvalues, eigenvectors = np.linalg.eig(A)
    
    ax.clear()
    
    # Unit circle
    theta = np.linspace(0, 2*np.pi, 100)
    circle = np.array([np.cos(theta), np.sin(theta)])
    ax.plot(circle[0], circle[1], 'k--', label='Unit Circle')
    
    # Transformed circle
    transformed_circle = A @ circle
    ax.plot(transformed_circle[0], transformed_circle[1], 'r', label='Transformed Circle')
    
    # Plot eigenvectors
    for i in range(len(eigenvalues)):
        vec = eigenvectors[:, i]
        ax.quiver(0, 0, vec[0], vec[1], angles='xy', scale_units='xy', scale=1, color='b', width=0.01)
        ax.quiver(0, 0, eigenvalues[i]*vec[0], eigenvalues[i]*vec[1], angles='xy', scale_units='xy', scale=1, color='g', width=0.01)
        ax.text(eigenvalues[i]*vec[0]*1.1, eigenvalues[i]*vec[1]*1.1, f'λ={eigenvalues[i]:.2f}', color='g')
    
    ax.set_xlim(-5,5)
    ax.set_ylim(-5,5)
    ax.set_aspect('equal')
    ax.grid(True)
    ax.legend()
    ax.set_title("Eigenvectors and Transformation of Unit Circle")
    fig.canvas.draw_idle()

# -----------------------------
# Plot setup
# -----------------------------
fig, ax = plt.subplots(figsize=(6,6))
plt.subplots_adjust(left=0.25, bottom=0.25)

plot_eigen(A)

# -----------------------------
# Sliders for matrix entries
# -----------------------------
axcolor = 'lightgoldenrodyellow'
ax_a = plt.axes([0.25, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_b = plt.axes([0.25, 0.10, 0.65, 0.03], facecolor=axcolor)
ax_c = plt.axes([0.25, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_d = plt.axes([0.25, 0.00, 0.65, 0.03], facecolor=axcolor)

s_a = Slider(ax_a, 'A[0,0]', -5.0, 5.0, valinit=A[0,0])
s_b = Slider(ax_b, 'A[0,1]', -5.0, 5.0, valinit=A[0,1])
s_c = Slider(ax_c, 'A[1,0]', -5.0, 5.0, valinit=A[1,0])
s_d = Slider(ax_d, 'A[1,1]', -5.0, 5.0, valinit=A[1,1])

def update(val):
    A_new = np.array([[s_a.val, s_b.val],
                      [s_c.val, s_d.val]])
    plot_eigen(A_new)

s_a.on_changed(update)
s_b.on_changed(update)
s_c.on_changed(update)
s_d.on_changed(update)

plt.show()
