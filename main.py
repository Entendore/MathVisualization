import numpy as np
import matplotlib.pyplot as plt
from scipy import misc
from utils.derivativeitegralslimits import compute_derivative, compute_integral
from utils.plotfunctions import plot_2d_data, plot_2d_fill, plot_3d_data, plot_2d_subplots, plot_3d_subplots, PlotData, PlotMultiData, Plots
from utils.animations import plot_3d_animation , plot_2d_animation
from utils.fouriertransform import generate_signal, compute_fourier_transform, plot_fourier_transform

if __name__ == "__main__":
     # Define a sample function
     func = lambda x: x**2  # Example: f(x) = x^2
     x_range = [-10, 10]  # Define the range of x
     x_range = np.linspace(x_range[0], x_range[1], 400)
     y_range = func(x_range)

     # Compute derivative
     x_derivative, y_derivative = compute_derivative(func, x_range)
     print("Numerical Derivative:")
     print(f"x values: {x_derivative}")
     print(f"Derivative values: {y_derivative}")

     # Compute integral
     integral_value = compute_integral(func, x_range)
     print("\nNumerical Integral:")
     print(f"Integral of f(x) from {x_range[0]} to {x_range[1]} is: {integral_value}")

     # Example usage
     figdata = PlotData(figsize=(8, 6), x=x_range , y=y_range,z=0, ranges=[-10, 10], marker="", color="blue", colorfill="yellow", 
                   makeredgecolor="", markerfacecolor="", Label="Data series", Labelfill="Fill series",
                   title="Derivatives", xlabel="X-axis", ylabel="Y-axis", 
                   grid=True, visible=True, linestyle="--", alpha=0.7, alphafill=0.5, legend=False)

     plot_2d_data(figdata)


     # Example usage
     figdata = PlotData(figsize=(8, 6), x=x_derivative , y=y_derivative,z=0, ranges=[-10, 10], marker="*", color="blue", colorfill="yellow",
                   makeredgecolor="red", markerfacecolor="green", Label="Data series", Labelfill="Fill series", 
                   title="Sample Plot", xlabel="X-axis", ylabel="Y-axis", 
                   grid=True, visible=True, linestyle="--", alpha=0.7, alphafill=0.5, legend=True)

     plot_2d_data(figdata)

     # Example usage
     figdata = PlotData(figsize=(8, 6), x=x_derivative , y=y_derivative,z=0, ranges=[-10, 10], marker="*", color="blue", colorfill="yellow",
                   makeredgecolor="red", markerfacecolor="green", Label="Data series", Labelfill="Fill series",
                   title="Sample Plot", xlabel="X-axis", ylabel="Y-axis", 
                   grid=True, visible=True, linestyle="--", alpha=0.7, alphafill=0.5, legend=True)

     plot_2d_fill(figdata)


     figdata = PlotMultiData(figsize=(8, 6), 
                    plots=[
                         PlotData(figsize=(8, 6), x=x_range , y=y_range,z=0, ranges=[-10, 10], marker="", color="blue", colorfill="yellow",makeredgecolor="red", markerfacecolor="green", Label="Data series", Labelfill="Fill series",title="Sample Plot", xlabel="X-axis", ylabel="Y-axis", grid=True, visible=True, linestyle="--", alpha=0.7, alphafill=0.5, legend=True),
                         PlotData(figsize=(8, 6), x=x_derivative , y=y_derivative,z=0, ranges=[-10, 10], marker="", color="blue", colorfill="yellow",makeredgecolor="red", markerfacecolor="green", Label="Data series", Labelfill="Fill series",title="Sample Plot", xlabel="X-axis", ylabel="Y-axis", grid=True, visible=True, linestyle="--", alpha=0.7, alphafill=0.5, legend=True)
                   ],
                   title="Sample Plot", xlabel="X-axis", ylabel="Y-axis", 
                   grid=True, visible=True, linestyle="--", alpha=0.7, alphafill=0.5, legend=True) 

     plot_2d_data(figdata)

     
    