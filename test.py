import numpy as np
import matplotlib.pyplot as plt
from scipy.misc import derivative
from scipy.integrate import quad

# Define the function
def func(x):
    return np.sin(x)  # Example function: sine wave

# Define the derivative and integral calculations
def numerical_derivative(func, x):
    return derivative(func, x, dx=1e-6)

def integral_from_zero(func, x):
    # Calculate the integral of the function from a fixed reference (e.g., 0)
    integral_values = []
    for val in x:
        integral, _ = quad(func, 0, val)  # Integral using scipy.integrate.quad
        integral_values.append(integral)
    return np.array(integral_values)

# Generate x values
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)

# Compute the function, derivative, and integral values
y = func(x)
dy_dx = np.array([numerical_derivative(func, xi) for xi in x])
integral_y = integral_from_zero(func, x)

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(x, y, label="Function (sin(x))", color='blue')
plt.plot(x, dy_dx, label="Derivative (cos(x))", color='orange')
plt.plot(x, integral_y, label="Integral", color='green')

# Add labels and title
plt.title("Function, Derivative, and Integral", fontsize=16)
plt.xlabel("x-axis (Input Values)", fontsize=12)
plt.ylabel("y-axis (Output Values)", fontsize=12, rotation=0, labelpad=60)  # Adjust label padding

# Add a legend
plt.legend(fontsize=12)

# Add grid for better visualization
plt.grid()

# Show the plot
plt.show()
