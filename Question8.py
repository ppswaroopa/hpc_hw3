from matplotlib import pyplot as plt
import numpy as np
from scipy.fftpack import fft

# Frequency in terms of Hertz
fre = 5
# Sample rate
fre_samp = 50
t = np.linspace(0, 2, 2 * fre_samp, endpoint=False)
a = np.sin(fre * 2 * np.pi * t)
figure, axis = plt.subplots()
axis.plot(t, a)
axis.set_xlabel('Time (s)')
axis.set_ylabel('Signal amplitude')
plt.show()

# do DFT and visualize:

dft = fft(a)
N = len(dft)
n = np.arange(N)
T = N/fre
frequency = n/T
dft = abs(dft)

figure_2, axis_2 = plt.subplots()
axis_2.plot(frequency, dft)
axis_2.set_xlabel('Frequency')
axis_2.set_ylabel('DFT Amplitude')
plt.show()
