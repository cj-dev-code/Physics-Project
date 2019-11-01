# -*- coding: utf-8 -*-
"""
Created on Thu Oct  3 17:33:31 2019

@author: josep
"""

import wave
import matplotlib.pyplot as plt
import numpy as np

from matplotlib.animation import FuncAnimation
file = wave.open("test.wav", 'rb')
# t = the time in seconds computed using the inverse framerate*the frame index
# amp = the integer amplitude at that time.

dualChannel = file.readframes(100000)
lChannel = dualChannel[::2]
rChannel = dualChannel[1::2]
frLen = file.getframerate()**-1

# Read all the wave data from the track into a dictionary of x and y coords
monoChannelLGraphData = {'t':[], 'amp':[]}
for i in range(0,len(lChannel),150):
    monoChannelLGraphData['t'].append(i*frLen)
    monoChannelLGraphData['amp'].append(lChannel[i])

# Hyperparameters
CLIPTIME = file.getframerate()**-1*file.getnframes()# x secs\frame * n frames
                                                    # = xn = total clip time(s)
FRAMERATE = file.getframerate()
PERCENT_OF_CLIPTIME_IN_VIEWING_WINDOW = .005
ANIMATION_FRAMES = PERCENT_OF_CLIPTIME_IN_VIEWING_WINDOW**-1 # 1 clip in how 
                                                    #     many viewing windows?
# Graph declarations and handles
graph_access_container = plt.figure()

# DECLARATION OF AMP_VS_TIME_PLOT
#   Used to graph the waveform across time t
amp_vs_time_plot = graph_access_container.add_subplot(1,1,1) 
viewing_window_size_in_seconds = CLIPTIME*PERCENT_OF_CLIPTIME_IN_VIEWING_WINDOW
amp_vs_time_plot.set_xlim([0, viewing_window_size_in_seconds]) # initial plot timeinterval
amp_vs_time_plot.set_ylim(ymax=200, ymin=20)
plot = amp_vs_time_plot.plot([], [], color = (0, 0, 1))
indexOfCurrentTime = 0
# Redraw all graphs at time time
def redraw(animationFrame): # takes the current animation frame we're on
    global indexOfCurrentTime
    currentTime = animationFrame * viewing_window_size_in_seconds
    while monoChannelLGraphData['t'][indexOfCurrentTime] < currentTime:
        indexOfCurrentTime+=1
    plot.set_xdata()
    if currentTime>viewing_window_size_in_seconds:
        lim = amp_vs_time_plot.set_xlim(currentTime-viewing_window_size_in_seconds,
                                       currentTime)
    else:
        # makes it look ok when the animation loops
        lim = amp_vs_time_plot.set_xlim(0, viewing_window_size_in_seconds)
    return amp_vs_time_plot
ani = animation.FuncAnimation(graph_access_container, redraw, frames=ANIMATION_FRAMES, 
                              interval=viewing_window_size_in_seconds, 
                              blit=False)
