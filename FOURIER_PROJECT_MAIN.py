# -*- coding: utf-8 -*-
"""
Created on Fri Nov  8 16:10:37 2019

@author: josep
"""

'''
MAIN PROJECT FILE FOR FOURIER TRANSFORM WORK

PROJECT DESCRIPTION:
    This project slides a .wav file through a window, graphically,
    displaying note decomposition of the "enwindowed" wav as it passes through
    
TODO:
    Write Framework to house .wav file, note decomposition
    Write Fourier Transform to be applied around time t
    Apply Fourier transform to .wav around time t
    Render .wav and transformed wav around time t
'''

# Get graphing, wav dependencies
import wave
from matplotlib.pylab import zeros, append, figure, subplot2grid
import matplotlib.animation as animation
import matplotlib

# Make the figure framework to hold the Transform and wav file
figure_1 = figure(num=0, figsize = (12, 9))
figure_1.suptitle("Wave Fourier Transform Analysis", fontsize=12)

# Make the axis
axis_1 = subplot2grid((2,2),(0,0), rowspan=1, colspan=2)    # The wav window
axis_2 = subplot2grid((2,2), (1, 0), rowspan=1, colspan=2)  # the transform win

axis_1.set_title("Song waveform")
axis_2.set_title("Notes comprising sound in Song waveform window")


# axis_1 rendering constants
WAVEFORM_WINDOW_WIDTH = 1 # How many seconds in width to render (s)
MAX_AMPLITUDE = 100 # Idk what this value is. Anna -- change it to what makes sense?
MIN_AMPLITUDE = 10  # likewise...


# axis_2 rendering constants
FREQUENCY_MAX = 200000  # max range of human hearing
FREQUENCY_MIN = 20      # min range of human hearing

# Set x limits for waveform and frequency domain
axis_1.set_xlim((0, WAVEFORM_WINDOW_WIDTH))  # Set the viewing window size
axis_2.set_xlim((FREQUENCY_MIN, FREQUENCY_MAX)) # Frequency range for our analysis

# Set y limits for waveform and frequency amplitude
axis_1.set_ylim((MIN_AMPLITUDE, MAX_AMPLITUDE))
axis_2.set_ylim((-MAX_AMPLITUDE, MAX_AMPLITUDE))

# Add grids to the axis
axis_1.grid(True)
axis_2.grid(True)

# Add labels to x axis of both axis_1 and axis_2
axis_1.set_xlabel("Time (s)")
axis_2.set_xlabel("Frequency (radian/sec)")

# Add labels to y axis of both axis_1 and axis_2
axis_1.set_ylabel("Amplitude")
axis_2.set_ylabel("Amplitude")

# Make data placeholders 
axis_1_data = zeros(0)
axis_2_data = zeros(FREQUENCY_MAX)

# Make data placeholders
axis_1_x = zeros(0)
axis_2_x = zeros(FREQUENCY_MAX)

wav_plot, = axis_1.plot(axis_1_x, axis_1_data, '-b', label='wave')
amp_freq, = axis_2.plot(axis_2_x, axis_2_data, '-b', label='Freqs')

axis_1.legend([wav_plot], [wav_plot.get_label()])
axis_2.legend([amp_freq], [amp_freq.get_label()])

def updateFunction(self):
    pass
    

simulation = animation.FuncAnimation(figure_1, updateFunction, blit=False, frames=200, interval=100, repeat=True)
matplotlib.pylab.plt.show()
