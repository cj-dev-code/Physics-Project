# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:08:34 2019

@author: josep
"""

from scipy.fftpack import fft
#import numpy.abs
from numpy import linspace, sin, cos, pi, absolute, arange
import numpy as np
import matplotlib.pyplot as plt

from scipy.io.wavfile import read

#file = wave.open("test.wav", 'rb')

#dualChannel = file.readframes(1200)
#lChannel = dualChannel[::2]
# Sample spacing
#frLen = file.getframerate()**-1
#x = np.linspace(0, N*T)
# Assumed mono audio
def apply_fourier_transformation(t_start, samp_sec, audio, snippet, amp_max, f_max, f_min=0):
    # snippet is the length of the audio slice on which to apply the transform
    t_end = t_start + snippet
    audio_selection = audio[int(samp_sec * t_start):int(samp_sec*t_end)]
    
    sec_samp = 1/samp_sec # seconds between samples
    N = len(audio_selection) # is the number of samples we are selecting
    freq_step = 10 # freq/index 
    
    #   Get the amplitudes from the fft without the imaginary part and 
    #   appropriately scaled
    amplitudes = absolute(fft(audio_selection)[0:int(N/2)])*2/N # Math from transform
    
    #f = Fs*np.arange((N/2))/N; # frequency vector
    f = samp_sec*arange((N/2))/N
    #(f_min, N/2, freq_step) # Maybe will be a breakpoint in testing?
    # Frequences start from zero
    idx_of_freq_min = int((f_min-f_min)/freq_step)
    idx_of_freq_max = int((f_max-f_min)/freq_step)
    
    return (f[idx_of_freq_min:idx_of_freq_max],
            amplitudes[idx_of_freq_min:idx_of_freq_max])

#lChannel = dualChannel[::2]
# Sample spacing
#frLen = file.getframerate()**-1


# SIMULATE SOME FRESH BEATS (Create an inorganic .wav file)
# list of audio_samples from wav file
# FOR TESTING PURPOSES: num_samples = 8000 # samples of audio taken (10 seconds for now)
# FOR TESTING PURPOSES: samp_sec = 800 # samples per second
# get real wav data
channel = 0 # the channel you're operating on
samp_sec, audio = read("ah-ee-ooh.wav")
#if len(audio) and len(audio[0]) - 1:
#    for i in range(len(audio)):
#        print(audio[i][channel])
#        audio[i] = audio[i][channel]
#        print(audio[i])
#        break
    
if len(audio) and len(audio[0]) - 1:
    audio = [amp[channel] for amp in audio]
else:
    audio = list(audio)
num_samples = len(audio)

sec_samp = samp_sec ** (-1) # seconds per sample
secs = sec_samp * num_samples
snippet = .1 # seconds to investigate per transform

#time_axis = linspace(0, sec_samp*num_samples, samp_sec*secs)
#audio = sin(50.0 * (2*pi*time_axis)) + .5*sin(80*(2*pi*time_axis)) # in amp

x, y = apply_fourier_transformation(.2, samp_sec, audio, snippet, 1, 500)

#plt.plot(time_axis, audio)
plt.plot(x, y)

#plt.ylim(0, 1)
#plt.xlim(0, len(x))
plt.grid()
plt.show()
'''
# Number of sample points
N = 20000
# sample spacing
T = 1.0 / N

k = 20 # k = an additional scalar

x = np.linspace(0.0, N*T, N)
y = np.sin(50.0 * 2.0*np.pi*x) + 0.5*np.sin(80.0 * 2.0*np.pi*x)
yf = fft(y)
xf = np.linspace(0.0, 1.0/(2.0*T), N//2)#1.0/(2.0*T), N//2)
import matplotlib.pyplot as plt
plt.plot(xf, 2.0/N * np.abs(yf[0:N//2])) # Some of the remaining math from the transform
plt.grid()
plt.show()
'''