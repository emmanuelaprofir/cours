import numpy as np
import random as rd
import copy

Y=[-1]*8
trouve =False

def acceptable(Y,nR,pos):
    if pos in Y:
        return False
    for x in range(0,nR):
        y=Y[x]
        if abs(x-nR)==abs(y-pos):
            return False
    return True

def remplir(Y,nR):
    global trouve
    if nR==8:
        trouve=True;return
    for pos in range(8):
        if acceptable(Y,nR,pos):
            Y[nR]=pos
            remplir(Y,nR+1)
            if trouve: return
            Y[nR]=-1

remplir(Y,0)