import numpy as np

# Function to compute the numerical derivative of a given function
def compute_derivative(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)  # Define x values
    y = func(x)  # Compute y values based on the function
    y_prime = np.gradient(y, x)  # Compute the derivative using numpy.gradient
    return x, y_prime  # Return x values and the derivative

# Function to compute the numerical integral of a given function
def compute_integral(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)  # Define x values
    y = func(x)  # Compute y values based on the function
    integral_value = np.trapz(y, x)  # Use trapezoidal rule for integration
    return integral_value, x, y  # Return the integral value and data for plotting

'''
# Function to compute the numerical integral of a given function
def compute_integral(func, x_range):
    x = np.linspace(x_range[0], x_range[1], 400)  # Define x values
    y = func(x)  # Compute y values based on the function
    integral_value = simpsonrule(y, x)  # Compute the total integral using Simpson's rule
    return integral_value  # Return the total integral value

# Custom Simpson's rule implementation
def simpsonrule(y, x):
    n = len(x)
    h = (x[-1] - x[0]) / (n - 1)
    return (h / 3) * (y[0] + y[-1] + 4 * sum(y[1:-1:2]) + 2 * sum(y[2:-2:2]))
'''