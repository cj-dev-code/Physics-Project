# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 10:41:32 2019

@author: josep
"""

import wave
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.pylab import zeros, append
from math import sin

import matplotlib.animation as animation


figure_1 = figure(num=0, figsize=  (12, 8))
figure_1.suptitle("SinFunction and Derivatives", fontsize=12)

axis_1 = subplot2grid((2, 2), (0, 0))
axis_2 = subplot2grid((2, 2), (0, 1))
axis_3 = subplot2grid((2, 2), (1, 0), colspan=2, rowspan=1)
axis_4 = axis_3.twinx()


# Set titles of subplots
axis_1.set_title('sin(x)')
axis_2.set_title("sin'(x)")
axis_3.set_title("sin''(x)")

# Change graph heights
axis_1.set_ylim((-1, 1))
axis_2.set_ylim((-1, 1))
axis_3.set_ylim((-1, 1))

# sex x-limits
axis_1.set_xlim(0,5.0)
axis_2.set_xlim(0,5.0)
axis_3.set_xlim(0,5.0)
axis_4.set_xlim(0,5.0)

# Try putting specific grid lines on different graphs
axis_1.grid(True)
axis_2.grid(False)
axis_3.grid(True)

# Set chart labels
axis_1.set_xlabel('x')
axis_2.set_xlabel('x')
axis_3.set_xlabel('x')

# y labels
axis_1.set_ylabel("sin(x)")
axis_2.set_ylabel("sin'(x)")
axis_3.set_ylabel("sin''(x)")

# I conjecture we need to set zeros on the graph to fill the starting data.
# Let me add them for now. This means the y axis are all going to be zero to 
# begin.
# Data for the y axis:
axis_1_data = zeros(0)
axis_2_data = zeros(0)
axis_3_data = zeros(0)
axis_4_data = zeros(0)
x = zeros(0) # We also need x values to be zeros too. This finished our placeholder data

# Time to make our plots! We plot the x and y data from each axis on the respective plots
# With titles nad line colors
sin_x_plot, = axis_1.plot(x, axis_1_data, 'b-',label="sin(x)")
sin_x_d1_plot, = axis_2.plot(x, axis_2_data, 'b-', label="sin'(x)")
sin_x_d2_plot, = axis_3.plot(x, axis_3_data, 'b-', label="sin''(x)")


# Then we add a legend. This consists of adding the lines we plotted associated with their names
# To the legend.
axis_1.legend([sin_x_plot], [sin_x_plot.get_label()])
axis_2.legend([sin_x_d1_plot], [sin_x_d1_plot.get_label()])
axis_3.legend([sin_x_d2_plot], [sin_x_d2_plot.get_label()])

x_t = 0 # starting theta = 0
max_t = 5

def updateFunction(self):
    global x_t, axis_1_data, axis_2_data, axis_3_data, axis_4_data, x
    
    #y = lambda x: sin(x)
    #dy_dx = lambda x: cos(x) 
    #y_dx_dx = lambda x: -sin(x)
    y = sin(x_t)# a list of points: y, let b be iter(y); next(b)
    dy_dx = cos(x_t) # like for a list of points: y, let b be iter(y); next(b)
    y_dx_dx = -sin(x_t) # like for a list of points: y, let b be iter(y); next(b)
    
    axis_1_data = append(axis_1_data, y)
    axis_2_data = append(axis_2_data, dy_dx)
    axis_3_data = append(axis_3_data, y_dx_dx)
    x = append(x, x_t)
    
    
    sin_x_plot.set_data(x, axis_1_data)
    sin_x_d1_plot.set_data(x, axis_2_data)
    sin_x_d2_plot.set_data(x, axis_3_data)
    
    x_t += 0.05
    
    if x_t >= max_t - 1.00:        
        sin_x_plot.axes.set_xlim(x_t-max_t+1.0,x_t+1.0)
        sin_x_d1_plot.axes.set_xlim(x_t-max_t+1.0,x_t+1.0)
        sin_x_d2_plot.axes.set_xlim(x_t-max_t+1.0,x_t+1.0)
        
        
    return sin_x_plot, sin_x_d1_plot, sin_x_d2_plot
    
simulation = animation.FuncAnimation(figure_1, updateFunction, blit=False, frames=200, interval=100, repeat=True)

matplotlib.pylab.plt.show()
# To recap:
#   We: 
#       Created our figure and 3 axis sets, one for each graph we want to show up
#       Gave names to our figure and our 3 axis sets. Thus we can reference them!
#       Set the graph's xlimits and y limits with respect to their standard dpi of 100
#       Added gridlines to our graphs.        
#       Added placeholder data to our graph,
#       Created line plots associated with each dataset for our plots. These are automatically added to our axis so they show up
#       Made a legend with the respective line plots we want to show on each graph

        