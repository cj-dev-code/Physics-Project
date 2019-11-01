# -*- coding: utf-8 -*-
"""
Created on Thu Sep 26 10:35:41 2019

@author: josep
"""

import matplotlib.pylab as plt
import matplotlib.animation as animation
import numpy as np

#create image with format (time,x,y)
image = np.random.rand(100,100,10)*20

#setup figure
fig = plt.figure()
grapher = fig.add_subplot(1,1,1)

#set up viewing window (in this case the 25 most recent values)
repeat_length = (np.shape(image)[0]+1)/4
grapher.set_xlim([0,repeat_length])

im2, = grapher.plot([], [], color=(0,0,1))
plt.ylim(ymax = 10, ymin = 0)
from functools import reduce
def func(n):
    im2.set_xdata(list(n + np.arange(10))*10)
    im2.set_ydata(reduce(lambda x, y: x+y, image[n].tolist()))
    
    #im2.set_ydata(image[0:n, 5, 5])
    
#    im2.set_xdata(np.arange(10))
 #   im2.set_ydata(image[n])
    
    if n>repeat_length:
       lim = grapher.set_xlim(n-repeat_length, n)
    else:
        # makes it look ok when the animation loops
        lim = grapher.set_xlim(0, repeat_length)
    return im2

ani = animation.FuncAnimation(fig, func, frames=image.shape[0], interval=30, blit=False)

plt.show()