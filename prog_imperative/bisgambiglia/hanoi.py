import numpy as np
import random as rd
import time

tA= [3,2,1]
tB = []
tC = []

def hanoi(n, t1, t2, t3, nom1, nom2, nom3):
    if n == 0: return
    hanoi(n-1, t1, t3, t2, nom1, nom3, nom2)
    t2.append(t1.pop())
    print(f"Deplacer {t2[-1]} de {nom1}->{nom2}")
    hanoi(n-1, t3, t2, t1, nom3, nom2, nom1)

hanoi(len(tA), tA, tB, tC, "tA", "tB", "tC")
