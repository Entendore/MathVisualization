import matplotlib.pyplot as plt
import numpy as np

class PlotData:
    def __init__(self, figsize=None, x=None, y=None, z=None,ranges=None, marker=None, color=None, colorfill=None, makeredgecolor=None, markerfacecolor=None, Label=None, Labelfill=None, title=None, xlabel=None, ylabel=None, grid=None, visible=None, linestyle=None, alpha=None, alphafill=None, legend=None,savepath=None):
        self.figsize = figsize
        self.x = x
        self.y = y
        self.z = z
        self.ranges=ranges
        self.marker = marker
        self.color = color
        self.colorfill= colorfill
        self.makeredgecolor = makeredgecolor
        self.markerfacecolor = markerfacecolor
        self.Label = Label
        self.labelfill = Labelfill
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.grid = grid
        self.visible = visible
        self.linestyle = linestyle
        self.alpha = alpha
        self.alphafill = alphafill
        self.legend = legend
        self.savepath = savepath


class Plots: 
    def __init__(self, x=None, y=None,z=None,ranges=None, marker=None, color=None, makeredgecolor=None, markerfacecolor=None, Label=None, Labelfill=None, alpha=None, alphafill=None,savepath=None):
        self.x = x
        self.y = y
        self.z = z
        self.ranges=ranges
        self.marker = marker
        self.color = color
        self.makeredgecolor = makeredgecolor
        self.markerfacecolor = markerfacecolor
        self.Label = Label
        self.labelfill = Labelfill
        self.alpha = alpha
        self.alphafill = alphafill
        self.savepath = savepath


class PlotMultiData:
    def __init__(self, figsize=None, plots=None, title=None, xlabel=None, ylabel=None, grid=None, visible=None, linestyle=None, alpha=None, legend=None, savepath=None):
        self.figsize = figsize
        self.plots = plots
        self.title = title
        self.xlabel = xlabel
        self.ylabel = ylabel
        self.grid = grid
        self.visible = visible
        self.linestyle = linestyle
        self.alpha = alpha
        self.legend = legend
        self.savepath = savepath

def plot_2d_data(figdata):
    # Create the plot
    plt.figure(figsize=figdata.figsize)

    plt.plot(figdata.x, figdata.y, marker= figdata.marker, color=figdata.color, mec=figdata.makeredgecolor, mfc=figdata.markerfacecolor, label=figdata.Label)
    
    # Add title and labels
    plt.title(figdata.title)
    plt.xlabel(figdata.xlabel)
    plt.ylabel(figdata.ylabel)

    # Show grid if enabled
    if figdata.grid:
        plt.grid(visible=figdata.visible, linestyle=figdata.linestyle, alpha=figdata.alpha)

    # Add a legend
    if figdata.legend:
        plt.legend()
    
    # Save the plot if a save path is provided
    if figdata.savepath:
        plt.savefig(figdata.savepath, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {figdata.savepath}")

    # Display the plot
    plt.show()


def plot_multiple_2d_data(figdata):
    # Create the plot
    plt.figure(figsize=figdata.figsize)

    for i, plot in enumerate(figdata.plots):
        plt.plot(plot.x, plot.y, marker= plot.marker, color=plot.color, mec=plot.makeredgecolor, mfc=plot.markerfacecolor, label=plot.Label)
    
    # Add title and labels
    plt.title(figdata.title)
    plt.xlabel(figdata.xlabel)
    plt.ylabel(figdata.ylabel)

    # Show grid if enabled
    if figdata.grid:
        plt.grid(visible=figdata.visible, linestyle=figdata.linestyle, alpha=figdata.alpha)

    # Add a legend
    if figdata.legend:
        plt.legend()

    # Save the plot if a save path is provided
    '''
    if figdata.savepath:
        plt.savefig(figdata.savepath, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {figdata.savepath}")
    '''

    # Display the plot
    plt.show()


def plot_2d_fill(figdata):

     # Create the plot
    plt.figure(figsize=figdata.figsize)

    plt.plot(figdata.x, figdata.y, marker= figdata.marker, color=figdata.color, mec=figdata.makeredgecolor, mfc=figdata.markerfacecolor, label=figdata.Label)
    plt.fill_between(figdata.x, figdata.y, color=figdata.colorfill, alpha=figdata.alphafill, where=(figdata.x >= figdata.ranges[0]) & (figdata.x <= figdata.ranges[1]), label=figdata.labelfill)

    # Add title and labels
    plt.title(figdata.title)
    plt.xlabel(figdata.xlabel)
    plt.ylabel(figdata.ylabel)

    # Show grid if enabled
    if figdata.grid:
        plt.grid(visible=figdata.visible, linestyle=figdata.linestyle, alpha=figdata.alpha)

    # Add a legend
    if figdata.legend:
        plt.legend()

    # Save the plot if a save path is provided
    if figdata.savepath:
        plt.savefig(figdata.savepath, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {figdata.savepath}")

    # Display the plot
    plt.show()

def plot_3d_data(figdata):
    # Create the plot
    plt.figure(figdata.size)
    plt.plot(figdata.x, figdata.y, figdata.z, marker=figdata.marker, label=figdata.Label)

    # Add title and labels
    plt.title(figdata.title)
    plt.xlabel(figdata.xlabel)
    plt.ylabel(figdata.ylabel)

    # Show grid if enabled
    if figdata.grid:
        plt.grid(visible=figdata.visible, linestyle=figdata.linestyle, alpha=figdata.alpha)

    # Add a legend
    plt.legend()

    # Save the plot if a save path is provided
    if figdata.savepath:
        plt.savefig(figdata.savepath, dpi=300, bbox_inches='tight')
        print(f"Plot saved to {figdata.savepath}")

    # Display the plot
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
    


def plot_3d_subplots(figInfo, fig, columns=3):
    # Get the number of subplots needed
    n_plots = len(figInfo)
    ncols = columns  # Set a fixed number of columns
    nrows = (n_plots // ncols) + (n_plots % ncols > 0)  # Calculate the required number of rows
    
    # Iterate over the figure information and plot each subplot
    for i, (x, y, z, title, xlabel, ylabel, zlabel, color, plot_type) in enumerate(figInfo):
        # Calculate subplot position
        row = i // ncols
        col = i % ncols
        ax = fig.add_subplot(nrows, ncols, i + 1, projection='3d')
        
        # Plot the data based on the plot_type
        if plot_type == 'scatter':
            ax.scatter(x, y, z, color=color)
        elif plot_type == 'line':
            ax.plot(x, y, z, color=color)
        elif plot_type == 'surface':
            ax.plot_surface(x, y, z, cmap='viridis')
        elif plot_type == 'wireframe':
            ax.plot_wireframe(x, y, z)
        elif plot_type == 'contour':
            ax.contour(x, y, z)
        elif plot_type == 'contourf':
            ax.contourf(x, y, z)
        elif plot_type == 'contour3D':
            ax.contour3D(x, y, z)
        else:
            raise ValueError("Invalid plot_type provided")

        # Set title and axis labels
        ax.set_title(title)
        ax.set_xlabel(xlabel)
        ax.set_ylabel(ylabel)
        ax.set_zlabel(zlabel)
        
        # Enable grid
        ax.grid()

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
