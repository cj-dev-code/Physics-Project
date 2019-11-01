# -*- coding: utf-8 -*-
"""
Created on Thu Oct 24 23:00:21 2019

@author: josep
"""

trial_data = [[1 + num for num in range(trial)] for trial in range(1, 10)]
def eliminationGame(trial):
    startFrom = True
    while len(trial) > 1:
        trial[:] = trial[startFrom::2]
        startFrom = not startFrom
    return trial[0]

for trial in trial_data[:10]:
    #if len(trial) % 2:#: or len(trial):
    print(trial, eliminationGame(trial[:]))