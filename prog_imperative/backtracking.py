import numpy as np
import random as rd

reseau = np.loadtxt("/Users/emmanuelaprofir/Documents/GitHub/cours/prog_imperative/lab.txt")
d=[0,0]
a=[reseau.shape[0]-1, reseau.shape[1]-1]
trouve = False

def acceptable(reseau, e):
    if e[0]<0 or e[0]>=reseau.shape[0]: return False
    if e[1]<0 or e[1]>=reseau.shape[1]: return False
    if reseau[e[0],e[1]]!=0: return False

    return True

def trouverUneSolution(reseau, ei):
    global trouve, a
    if a == ei:
        trouve = True ; return
    for direction in [[0,1],[1,0],[0,-1],[-1,0]]:
        e = [ei[0]+direction[0], ei[1]+direction[1]]
        if acceptable(reseau,e):
            reseau[ei[0],ei[1]]=1
            trouverUneSolution(reseau,e)
            if trouve :return
            reseau[ei[0], ei[1]]=0

trouverUneSolution(reseau,d)
print(reseau)