import numpy as np
import matplotlib.pyplot as plt


def main():
    # x values range = [0, 10] with 100 points.
    x = np.linspace(0, 10, 100)
    # y value is sin(x)
    y = np.sin(x)
    y1 = np.convolve(x, np.sin(x))
    
    plt.subplot(3, 1, 1)
    plt.title("Before")
    plt.plot(x, y)
    plt.ylabel("sin(x)")
    plt.grid(True)

    plt.subplot(3, 1, 2)
    plt.plot(np.arange(0, len(y1), 1), y1)
    plt.title("After")
    plt.ylabel("cos(x)")
    plt.xlabel("x")
    plt.grid(True)

    plt.subplot(3, 1, 3)
    plt.plot(x, x**2)

    plt.show()

main()

