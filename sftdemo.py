# -*- coding: utf-8 -*-

# demo slow Fourier transfor program
# translated to Python from the original Matlab in Numerical Methods for
# Physics by Alejandro L. Garcia, 1994.

import numpy as np
import matplotlib.pyplot as plt


def main():
    N = int(input("Enter the number of points N - "))
    freq = float(input("Enter the frequency of the sine wave - "))
    phase = float(input("Enter the phase of the sine wave - "))

    tau = 1  # time increment
    t = np.arange(0, N)*tau  # array goes from 0..N-1
    y = np.sin(2*np.pi*t*freq + phase)  # sine wave data set

    # compute discrete Fourier transform
    yt = sft(y)
    # frequency vector
    f = np.arange(0, N)/(N * tau)

    # plot the original data and its Fourier transform
    _, axs = plt.subplots(1, 2)
    axs[0].set(title="Original data set")
    axs[0].set_xlabel("Time")
    axs[0].set_ylabel("Amplitude")
    axs[0].plot(t, y)

    axs[1].set(title="Real (solid); Imag(dash)")
    axs[1].set_xlabel("Frequency")
    axs[1].set_ylabel("Fourier transform")
    axs[1].plot(f, np.real(yt), f, np.imag(yt), '--')

    plt.savefig("dft-sine-wave.png")
    plt.show()


def sft(y):
    # slow Fourier transform
    N = len(y)
    twopiN = -2*np.pi*1j/N  # note: j is sqrt(-1)

    yt = np.arange(0, N, dtype=np.cdouble)
    for k in range(0, N):
        temp = np.exp(twopiN*np.arange(0, N)*k)
        yt[k] = np.sum(np.vdot(y, temp))

    return yt


if __name__ == "__main__":
    main()


# vim: expandtab shiftwidth=4 softtabstop=4
