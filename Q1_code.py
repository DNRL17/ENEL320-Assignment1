import numpy as np
import matplotlib.pyplot as plt
from scipy import signal


def main():

    # Generate data
    t = np.linspace(-10*np.pi, 10*np.pi, 1000)
    f = signal.square(t, 0.5) * np.sin(t)
    #f = np.heaviside(t, 0.5)

    # Initialize plots
    fig, ax = plt.subplots(2, 1)
    fig.tight_layout(h_pad=2)

    # Define figures
    ax[0].plot(t, f)
    ax[1].plot(t, np.fft.fft(f))

    # Define subplot titles
    ax[0].set_title('Original Signal')
    ax[1].set_title('Signal in Fourier Space')

    # Add grids
    ax[0].grid(True)
    ax[1].grid(True)

    # Name and scale figure
    fig.suptitle('Modelling a Real-World Signal')
    plt.subplots_adjust(top=0.85)

    plt.show()

main()

