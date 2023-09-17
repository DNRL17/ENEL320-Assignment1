# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 21:43:29 2023

@author: BMA191 DNRL17
"""

from scipy import signal
import sounddevice as sd
import matplotlib.pyplot as plt
import numpy as np
from numpy.fft import fft, ifft

#-------Modulation for the moddeled wave-----
def modulation(msg, mod):
    return (msg*mod)

#-------Demodulation for the moddeled wave ----
def demodulation(St, x, noise):
    St[St < 0] = 0
    St += noise
    return lpfilter(St)

#-------Demodulation for the song--------
def songdemodulation(St, x, noise):
    St[St < 0] = 0
    St += noise
    return bpfilter(St)


#-------Low pass filter for the model wave----
def lpfilter(St):
    sos = signal.butter(10, 500, 'lp', fs=44100, output='sos')
    return signal.sosfilt(sos,St)

#-------band pass filter for the song--------
def bpfilter(St):
    sos = signal.butter(10, [100,2000], 'bp', fs=44100, output='sos')
    return signal.sosfilt(sos,St)

#-------Main for the model wave------
def basic():
    Ac = 5
    u = 0.5
    x = np.linspace(0, 10000, 100000)
    mod = np.cos(2*np.pi*x*26500)
    msg = Ac*(1+u*(np.cos(2*np.pi*200*x)))
    noise = np.random.normal(0, 0.05 * np.std(msg), size = msg.shape)
    
    St = modulation(msg, mod)
    Mout = demodulation(St, x, noise)
    
    plt.plot(x, Mout)

    plt.title("Output Model Waveform u = 1")
    plt.xlabel("Time (s)")
    plt.ylabel("Message")
    
    plt.show()  

#-------Main for the song----------
def song():
    x = np.linspace(0, 107768, 107768)
    y = np.loadtxt('am_mystery_song.txt')
    noise = np.random.normal(0, 0.5 * np.std(y), size = y.shape)
    Mout = songdemodulation(y, x, noise)

    sd.play(Mout, 44100)
    plt.plot(x, Mout)

    plt.title("Song Waveform With Noise")
    plt.xlabel("Time (s)")
    plt.ylabel("Message")
    
    plt.show()
song()