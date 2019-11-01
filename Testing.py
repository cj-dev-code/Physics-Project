# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 14:27:24 2019

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
clipTime = frLen*file.getnframes()  # Total clip length
FRAMEWIDTH = .1                     # Length the viewing area in seconds
num_anim_frames = 20                # The number of frames
interval = clipTime/num_anim_frames


fig = plt.figure()
ax = plt.axes(xlim=(0, FRAMEWIDTH), ylim=(-0, 250))
line, = ax.plot([], [], lw=3)


def init():
    line.set_data([], [])
    return line,

def animate(i):
    print(i)
    # convert i to time
    i *= interval
    x = monoChannelLGraphData['t']
    
    startInd = 0
    while x[startInd] < i and startInd < len(x)-1:
        startInd += 1
    endInd = startInd
    while x[endInd] < i + FRAMEWIDTH and endInd < len(x)-1:
        endInd += 1
    
    
    x = x[startInd:endInd]
    y = monoChannelLGraphData['amp'][startInd:endInd]
    print(x, y)
    
    #plt.xticks(x, horizontalalignment='left')
    plt.axes.set_xlim(startInd, endInd)
    return line,

anim = FuncAnimation(fig, animate, init_func=init,
                               frames=num_anim_frames, interval=interval, blit=True)
anim.save('sine_wave_3.gif', writer='imagemagick')

#plt.ylim((25,250))
#plt.plot('t','amp', monoChannelLGraphData)
plt.plot(monoChannelLGraphData['t'],monoChannelLGraphData['amp'])
file.close()

import graphics as g
def testBox(width, height, zoom, t_scale):
    win = g.GraphWin('Test',width,height)
    head = g.Circle(g.Point(100, 100), 25)
    head.draw(win)
    
    # Make the bar to measure the time of the video
    T_SCALE_POS = (width * .1, height * .9)
    NUM_TICKS = 10
    TICK_SEMI_HEIGHT = 5
    t_scale_segs = [g.Line(g.Point(T_SCALE_POS[0], T_SCALE_POS[1]), 
                           g.Point(width - T_SCALE_POS[0], T_SCALE_POS[1]))]
    t_scale_segs += [g.Line(g.Point(T_SCALE_POS[0] + i * (width*.8/NUM_TICKS), T_SCALE_POS[1]-TICK_SEMI_HEIGHT),
                            g.Point(T_SCALE_POS[0] + i * (width*.8/NUM_TICKS), T_SCALE_POS[1]+TICK_SEMI_HEIGHT)) for i in range(NUM_TICKS + 1)]
    
    for seg in t_scale_segs:
        seg.draw(win)
    #t_scale_segs[0].setWidth(1)
    #t_scale_segs[0].draw(win)

    return win

WIDTH, HEIGHT = 500, 300
win = testBox(WIDTH, HEIGHT, 0, 0)
