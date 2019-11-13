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
    
TODO:
    Sync up t progression to system time?
'''

# Get graphing, wav dependencies
from scipy.fftpack import fft
from matplotlib.pylab import zeros, append, figure, subplot2grid
from scipy.io.wavfile import read
from numpy import absolute, arange
import matplotlib.animation as animation
import matplotlib
import simpleaudio as sa
import threading

from datetime import datetime


# Transforms audio range in amp vs. time to amp vs. freq
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
    
    # f = frequency vector
    f = samp_sec*arange((N/2))/N 
    #(f_min, N/2, freq_step) # Maybe will be a breakpoint in testing?
    # Frequences start from zero
    idx_of_freq_min = int((f_min-f_min)/freq_step)
    idx_of_freq_max = int((f_max-f_min)/freq_step)
    
    return (f[idx_of_freq_min:idx_of_freq_max],
            amplitudes[idx_of_freq_min:idx_of_freq_max])


def updateFunction(self):
    global t_start, samp_sec, audio, snippet, amp_max, freq_max, freq_min
    amp_freq.set_data(*apply_fourier_transformation(t_start, samp_sec, audio,
                                                     snippet, amp_max, freq_max,
                                                     freq_min))
    axis_2.set_xlim(freq_min, freq_max)
    axis_2.set_ylim(0, amp_max)
    time_elapsed = datetime.now() - song_start_time
    t_start = time_elapsed.seconds + time_elapsed.microseconds/10**6
    
    #print(time_elapsed)
    return wav_plot, amp_freq

filename = "tiktok.wav"

channel = 0 # the channel you're operating on
samp_sec, audio = read(filename)

# convert stereo audio to mono audio if need be
if len(audio) and len(audio[0]) - 1:
    audio = [amp[channel] for amp in audio]
else:
    audio = list(audio)

num_samples = len(audio)
sec_samp = samp_sec ** (-1) # seconds per sample
secs = sec_samp * num_samples
snippet = .1 # seconds to investigate per transform

t_start = 0
amp_max = 5000
freq_min = 0
freq_max = 4000


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
# None
# Set x limits for waveform and frequency domain
axis_1.set_xlim((0, WAVEFORM_WINDOW_WIDTH))  # Set the viewing window size
#axis_2.set_xlim((FREQUENCY_MIN, FREQUENCY_MAX)) # Frequency range for our analysis

# Set y limits for waveform and frequency amplitude
axis_1.set_ylim((MIN_AMPLITUDE, MAX_AMPLITUDE))
#axis_2.set_ylim((-MAX_AMPLITUDE, MAX_AMPLITUDE))

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
axis_2_data = zeros(0)

# Make data placeholders
axis_1_x = zeros(0)
axis_2_x = zeros(0)

wav_plot, = axis_1.plot(axis_1_x, axis_1_data, '-b', label='wave')
amp_freq, = axis_2.plot(axis_2_x, axis_2_data, '-b', label='Amps')

axis_1.legend([wav_plot], [wav_plot.get_label()])
axis_2.legend([amp_freq], [amp_freq.get_label()])

wave_obj = sa.WaveObject.from_wave_file(filename)
t = threading.Thread(target=wave_obj.play, name="Play Wav")
t.daemon = True
song_start_time = datetime.now()
t.start()
simulation = animation.FuncAnimation(figure_1, updateFunction, blit=False, frames=200, interval=10, repeat=True)
matplotlib.pylab.plt.show()