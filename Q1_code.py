import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fft



def main():

    # Generate data
    fs = 1 # Sine frequency
    N = 1000 # Samples
    t = np.linspace(-10*np.pi, 10*np.pi, N) # Time axis 
    freq = np.fft.fftfreq(t.size, (20*np.pi)/N) # Frequency domain axis

    sig = (signal.square(t, 0.5) + 1) * np.sin(fs*2*np.pi*t) # Ideal Doppler wave signal (no noise)
    noise = np.random.normal(0, .5, sig.shape) # Generate random noise
    noisy_sig = sig + noise

    # Initialize plots
    fig, ax = plt.subplots(2, 2)
    fig.tight_layout(h_pad=2)

    # Define figures
    ax[0][0].plot(t, sig)
    ax[1][0].plot(freq, fft.fft(sig))

    # Noisy Signals
    ax[0][1].plot(t, noisy_sig)
    ax[1][1].plot(freq, fft.fft(noisy_sig))

    # Define subplot titles
    ax[0][0].set_title('Ideal Signal')
    ax[1][0].set_title('Ideal Signal in Fourier Space')
    ax[0][1].set_title("Realistic Signal with Noise")
    ax[1][1].set_title("Fourier Transform of Noisy Signal")

    # Add grids
    ax[0][0].grid(True)
    ax[1][0].grid(True)
    ax[0][1].grid(True)
    ax[1][1].grid(True)

    # Name and scale figure
    fig.suptitle('Modelling a Real-World Sonar Pulse')
    plt.subplots_adjust(top=0.85)

    plt.show()

main()

