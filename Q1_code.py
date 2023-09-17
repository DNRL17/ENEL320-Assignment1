import numpy as np
import matplotlib.pyplot as plt
from scipy import signal
from scipy import fft



def main():

    # Generate data
    fs = 1 # Sine frequency
    N = 2000 # Samples
    t = np.linspace(-10*np.pi, 10*np.pi, N) # Time axis 
    #tf = np.fft.fftfreq(N, 1/(5*fs))
    #freq = np.fft.fftfreq(t.shape[-1])
    sig = (signal.square(t, 0.5) + 1) * np.sin(fs*2*np.pi*t)

    # Initialize plots
    fig, ax = plt.subplots(2, 1)
    fig.tight_layout(h_pad=2)

    # Define figures
    ax[0].plot(t, sig)
    ax[1].plot(t, fft.fft(np.sin(fs*2*np.pi*t)))

    # Define subplot titles
    ax[0].set_title('Original Signal')
    ax[1].set_title('Signal in Fourier Space')

    # Add grids
    ax[0].grid(True)
    ax[1].grid(True)

    # Name and scale figure
    fig.suptitle('Modelling a Real-World Sonar Pulse')
    plt.subplots_adjust(top=0.85)

    plt.show()

main()

