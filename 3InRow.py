# -*- coding: utf-8 -*-
"""
Created on Mon Jan 29 10:38:30 2018

@author: p.castro.sampol
"""

import numpy as np

def threeInRow(x,y,z) :
    return (x & y & z) == (x|y|z)

def checkWinner(positions) :
    if (threeInRow(positions[0],positions[1],positions[2]) != 0) :
        return (positions[0] & positions[1] & positions[2])
    if (threeInRow(positions[0],positions[3],positions[6]) != 0) :
        return (positions[0] & positions[3] & positions[6])
    if (threeInRow(positions[3],positions[4],positions[5]) != 0) :
        return (positions[3] & positions[4] & positions[5])
    if (threeInRow(positions[6],positions[7],positions[8] != 0)) :
        return (positions[6] & positions[7] & positions[8]) 
    if (threeInRow(positions[1],positions[4],positions[7] != 0)) :
        return (positions[1] & positions[4] & positions[7])
    if (threeInRow(positions[2],positions[5],positions[8] != 0)) :
        return (positions[2] & positions[5] & positions[8])
    if (threeInRow(positions[0],positions[4],positions[8] != 0)) :
        return (positions[0] & positions[4] & positions[8])
    if (threeInRow(positions[2],positions[4],positions[6] != 0)) :
        return (positions[2] & positions[4] & positions[6])
    return 0

def endGame(positions):
    win = checkWinner(positions)
    if win == 0 and np.count_nonzero(positions) == 9 :
        return 0
    if win == 0:
        return False
    return win


positions = np.zeros(9)
pesos = []
#while endGame(positions) == False :
#    positions = 0





