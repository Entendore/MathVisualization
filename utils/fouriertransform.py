import numpy as np
import matplotlib.pyplot as plt

def generate_signal(frequencies, duration, sampling_rate):
    T = 1 / sampling_rate  # Sampling interval
    t = np.arange(0, duration, T)  # Time vector
    signal = sum(np.sin(2 * np.pi * f * t) for f in frequencies)
    return t, signal

def compute_fourier_transform(signal, sampling_rate):
    n = len(signal)
    fft_result = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(n, 1 / sampling_rate)
    fft_magnitude = np.abs(fft_result)
    return frequencies[:n // 2], fft_magnitude[:n // 2]


def plot_fourier_transform(signal, sampling_rate):
    """
    Plot the original signal and its Fourier Transform.

    Parameters:
    - signal: The signal array (time-domain data).
    - sampling_rate: Sampling rate of the signal in Hz.

    Returns:
    - frequencies: Array of positive frequency components.
    - fft_values: Array of corresponding FFT magnitude values.
    """
    # Perform the Fourier Transform
    fft_values = np.fft.fft(signal)
    frequencies = np.fft.fftfreq(len(signal), d=1/sampling_rate)

    # Only keep the positive frequencies
    positive_freqs = frequencies > 0
    fft_values = fft_values[positive_freqs]
    frequencies = frequencies[positive_freqs]

    # Plot the original signal
    time = np.arange(0, len(signal)) / sampling_rate
    plt.figure(figsize=(12, 6))

    plt.subplot(2, 1, 1)
    plt.plot(time, signal)
    plt.title("Original Signal")
    plt.xlabel("Time [s]")
    plt.ylabel("Amplitude")

    # Plot the magnitude of the Fourier Transform
    plt.subplot(2, 1, 2)
    plt.plot(frequencies, np.abs(fft_values))
    plt.title("Fourier Transform")
    plt.xlabel("Frequency [Hz]")
    plt.ylabel("Magnitude")

    plt.tight_layout()
    plt.show()

    return frequencies, np.abs(fft_values)
