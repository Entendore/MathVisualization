import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def plot_2d_animation(x_func, y_func, frames, xlim, ylim, interval=50, save_as=None):
    fig = plt.figure()  # Create a figure
    ax = fig.add_axes([0, 0, 1, 1])  # Full-figure axis
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    line, = ax.plot([], [], lw=2)  # Create an empty line to animate

    def init():
        """Initialize the line."""
        line.set_data([], [])
        return line,

    def update(frame):
        """Update the line for each frame."""
        x = x_func(frame)
        y = y_func(frame)
        line.set_data(x, y)
        return line,

    # Create the animation
    ani = FuncAnimation(fig, update, frames=frames, init_func=init, interval=interval, blit=True)
    
    # Save the animation if required
    if save_as:
        ani.save(save_as, writer='ffmpeg')
    
    plt.show()

def plot_2d_subplots(figInfo, fig, columns=3):
    
    # Get the number of subplots needed
    n_plots = len(figInfo)
    ncols = columns  # Set a fixed number of columns
    nrows = (n_plots // ncols) + (n_plots % ncols > 0)  # Calculate the required number of rows

    # Iterate over the figure information and plot each subplot
    for i, (x, y, title, xlabel, ylabel, color, line_style, plot_type) in enumerate(figInfo):
        # Calculate subplot position
        row = i // ncols
        col = i % ncols
        f = fig.add_subplot(nrows, ncols, i + 1)
        
        # Plot the data based on the plot_type
        if plot_type == 'scatter':
            f.scatter(x, y, color=color)
        elif plot_type == 'line':
            f.plot(x, y, color=color, linestyle=line_style)
        elif plot_type == 'bar':
            f.bar(x, y, color=color)
        elif plot_type == 'histogram':
            f.hist(x, bins=10, color=color)
        elif plot_type == 'pie':
            f.pie(y, labels=x, colors=color)
        elif plot_type == 'boxplot':
            f.boxplot(x, vert=False, colors=color)  
        elif plot_type == 'violin':
            f.violinplot(x, vert=False, colors=color)
        elif plot_type == 'errorbar':
            f.errorbar(x, y, fmt='o', color=color)
        else:
            raise ValueError("Invalid plot_type provided")

        # Set title and axis labels
        f.set_title(title)
        f.set_xlabel(xlabel)
        f.set_ylabel(ylabel)
        
        # Enable grid
        f.grid()

    # Adjust layout
    plt.tight_layout()

    # Display the plot
    plt.show()
    


def plot_3d_animation(x_func, y_func, z_func, frames, xlim, ylim, zlim, interval=50, save_as=None):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.set_xlim(xlim)
    ax.set_ylim(ylim)
    ax.set_zlim(zlim)
    line, = ax.plot([], [], [], lw=2)

    def init():
        line.set_data([], [])
        line.set_3d_properties([])
        return line,

    def update(frame):
        x = x_func(frame)
        y = y_func(frame)
        z = z_func(frame)
        line.set_data(x, y)
        line.set_3d_properties(z)
        return line,

    ani = FuncAnimation(fig, update, frames=frames, init_func=init, interval=interval, blit=False)
    
    if save_as:
        ani.save(save_as, writer='ffmpeg')
    
    plt.show()


def plot_3d_subplots(figInfo, fig, columns=3):
    
    # Get the number of subplots needed
    n_plots = len(figInfo)
    ncols = columns  # Set a fixed number of columns
    nrows = (n_plots // ncols) + (n_plots % ncols > 0)  # Calculate the required number of rows
    
    # Iterate over the figure information and plot each subplot
    for i, (x, y, z, title, xlabel, ylabel, zlabel, color, style, plot_type) in enumerate(figInfo):
        # Calculate subplot position
        row = i // ncols
        col = i % ncols
        f = fig.add_subplot(nrows, ncols, i + 1, projection='3d')
        
        # Plot the data based on the plot_type
        if plot_type == 'scatter':
            f.scatter(x, y, z, color=color)
        elif plot_type == 'line':
            f.plot(x, y, z, color=color)
        elif plot_type == 'surface':
            f.plot_surface(x, y, z, cmap='viridis')
        elif plot_type == 'wireframe':
            f.plot_wireframe(x, y, z)
        elif plot_type == 'contour':
            f.contour(x, y, z)
        elif plot_type == 'contourf':
            f.contourf(x, y, z)
        elif plot_type == 'contour3D':
            f.contour3D(x, y, z)
        else:
            raise ValueError("Invalid plot_type provided")

        # Set title and axis labels
        f.set_title(title)
        f.set_xlabel(xlabel)
        f.set_ylabel(ylabel)
        f.set_zlabel(zlabel)
        
        # Enable grid
        f.grid()

    # Adjust layout to avoid overlap and show the plot
    plt.tight_layout()
    plt.show()

def plot_unit_circle():
    """
    Plots a unit circle with cosine and sine labels at every 45 degrees.
    """
    # Create a figure and axis
    fig, ax = plt.subplots(figsize=(6, 6))

    # Generate points for the unit circle
    theta = np.linspace(0, 2 * np.pi, 500)  # Angles from 0 to 2π
    x = np.cos(theta)  # x-coordinates
    y = np.sin(theta)  # y-coordinates

    # Plot the unit circle
    ax.plot(x, y, label="Unit Circle", color="blue")

    # Highlight key points at 45° intervals and label sin/cos
    angles = np.arange(0, 360, 45)  # Angles in degrees
    for angle in angles:
        rad = np.radians(angle)  # Convert angle to radians
        cos_val = np.cos(rad)
        sin_val = np.sin(rad)

        # Plot points on the circle
        ax.plot(cos_val, sin_val, 'ro')  # Red dots at key points

        # Label cosine and sine values
        ax.text(cos_val * 1.1, sin_val * 1.1, 
                f"cos={cos_val:.2f}\nsin={sin_val:.2f}", 
                fontsize=9, ha='center', va='center', 
                bbox=dict(boxstyle="round,pad=0.3", edgecolor='gray', facecolor='white'))

    # Add grid lines and axis
    ax.axhline(0, color='black', linewidth=0.5, linestyle='--')
    ax.axvline(0, color='black', linewidth=0.5, linestyle='--')
    ax.grid(color='gray', linestyle='--', linewidth=0.5)

    # Set axis limits
    ax.set_xlim(-1.5, 1.5)
    ax.set_ylim(-1.5, 1.5)

    # Equal aspect ratio to ensure the circle looks circular
    ax.set_aspect('equal', adjustable='box')

    # Add labels and title
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_title("Unit Circle with Cosine and Sine Labels")
    ax.legend()

    # Show the plot
    plt.show()

    