# -*- coding: utf-8 -*-
"""
Created on Tue Sep 24 22:28:15 2019

@author: josep
"""

from random import randrange,seed
import numpy as np
import matplotlib.pyplot as plt


def shuffle(deck_1, deck_2):
    # true shuffle
    i = 1
    while i < 52:
        randomInd = randrange(0, i+1)
        deck_1[randomInd], deck_1[i] = deck_1[i], deck_1[randomInd]
        i+=1
        
    i = 1
    
    while i < 52:
        randomInd_1, randomInd_2 = randrange(0, 52), randrange(0, 52)
        deck_2[randomInd_1], deck_2[randomInd_2] = (deck_2[randomInd_2],
                                                    deck_2[randomInd_1])
        i+=1
   
def main():
    seed(2)
    for number in range(52):
        print("TRIAL", number)
        trials = 1000
        deckSize = 52
        solution_set_1 = [[]*deckSize]*trials
        solution_set_2 = [[]*deckSize]*trials
        for trial in range(trials):
            # True shuffle deck
            deck_1 = [i + 1 for i in range(52)]
            # False shuffle deck
            deck_2 = [i + 1 for i in range(52)]
            shuffle(deck_1, deck_2)
            solution_set_1[trial] = deck_1[number]
            solution_set_2[trial] = deck_2[number]
        plt.hist(solution_set_1, bins = 52)
        plt.show()
        plt.hist(solution_set_2, bins = 52)
        plt.show()
        number_of_times_one_shows_up = solution_set_2.count(1)
        numter_of_times_two_shows_up = solution_set_2.count(2)
        print(number_of_times_one_shows_up)
        print(numter_of_times_two_shows_up)

main()