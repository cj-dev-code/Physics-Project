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
figure_1 = figure(num=0, figsize = (12, 8))
figure_1.suptitle("Wave Fourier Transform Analysis", fontsize=12)

# Make the axis
axis_1 = subplot2grid((2,2),(0,0), rowspan=1, colspan=2)    # The wav window
axis_2 = subplot2grid((2,2), (1, 0), rowspan=1, colspan=2)  # the transform win

axis_1.set_title("Song waveform")
axis_2.set_title("Notes comprising sound in Song waveform window")


# axis_1 rendering constants
WAVEFORM_WINDOW_WIDTH = 1 # How many seconds in width to render (s)
WAVEFORM_MAX_AMPLITUDE = 100 # Idk what this value is. Anna -- change it to what makes sense?
WAVEFORM_MIN_AMPLITUDE = 10  # likewise...


# axis_2 rendering constants
FREQUENCY_MAX = 200000  # max range of human hearing
FREQUENCY_MIN = 20      # min range of human hearing

axis_1.set_xlim(WAVEFORM_WINDOW_WIDTH)  # Set the viewing window size
axis_2.set_xlim((FREQUENCY_MIN, FREQUENCY_MAX)) # Frequency range for our analysis

axis_1.set_ylim((FREQUENCY_MIN, FREQUENCY_MAX))
axis_2.set_ylim((-FREQUENCY_MAX, FREQUENCY_MAX))