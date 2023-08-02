import numpy as np
import matplotlib.pyplot as plt


def main():

    # x values range = [0, 20pi] with 1000 points.
    x = np.linspace(0, 20*np.pi, 1000)


    message = np.sin(x)
    carrier = np.cos(x)

    result = np.convolve(message, carrier)
    
    # First subplot: rows, cols, index. Shows message signal. #TODO Currently random placeholder plot.
    plt.subplot(3, 1, 1)
    plt.title("Message")
    plt.plot(x, message)
    plt.ylabel("sin(x)")
    plt.grid(True)

    # Second subplot: Shows carrier signal. #TODO Currently random placeholder plot.
    plt.subplot(3, 1, 2)
    plt.title("Carrier")
    plt.plot(x, carrier)
    plt.grid(True)


    # Third subplot: Shows resulting signal. #TODO Currently random placeholder plot.
    plt.subplot(3, 1, 3)
    plt.plot(x, result[:len(x)])
    plt.title("Result")
    #plt.ylabel("cos(x)")
    plt.xlabel("x")
    plt.grid(True)

    plt.show()

main()

