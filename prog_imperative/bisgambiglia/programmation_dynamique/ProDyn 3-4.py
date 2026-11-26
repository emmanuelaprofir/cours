import numpy as np
import copy
import math

objets = np.loadtxt("Sac a dos.txt", dtype=int)

########### Q1 - Couts récursive ###########
def couts_recursive(Taille):
    global objets
    C=np.zeros([objets.shape[0], Taille+1])
    for i in range(1,objets.shape[0]):
        for w in range(1,Taille+1):
            cn, wn=objets[i,1], objets[i,2]
            if w<wn : C[i,w]=C[i-1,w]
            else :
                C[i,w]=max(C[i-1,w], C[i-1,w-wn]+cn)
    return C

    # test de la Q1
#C=couts_recursive(15)

########### Q2 - Liste des objets dans le sac ###########

def liste_objets(poids, C) :
    w=poids
    sac=[]
    i=objets.shape[0]-1
    while w>0 and i>0 :
        wn = objets[i,2]
        if C[i,w]!=C[i-1,w] : 
            sac.append(i)
            w=w-wn
        i=i-1
    return sac

    # test de la Q2
#sac = liste_objets(15,C)

"""----------------------------------------------
        Exercice 4 : infiltration
   ----------------------------------------------"""
couches = np.loadtxt("Infiltration.txt", dtype=int)
solution={"Cellules" : [], "Durée" : math.inf}
chemin={"Cellules" : [], "Durée" : 0}


########### Q1 - Infiltration récursive ###########

def acceptable(e):
    global couches
    if e<0 : return False
    if e>=couches.shape[1] : return False
    return True
    
def infiltration(c, ei):
    global couches, solution, chemin
    if c==couches.shape[0] :
        if chemin["Durée"]<solution["Durée"] :
            solution=copy.deepcopy(chemin)
        return
    if couches[c,ei]==-1 : return False
    for e in [ei-1, ei, ei+1] :
        if acceptable(e):
            chemin["Cellules"].append(ei)
            chemin["Durée"] += couches[c,ei]
            infiltration(c+1, e)
            chemin["Cellules"].pop() 
            chemin["Durée"] -= couches[c,ei]
            
    # test de la Q1            
#infiltration(0,1)

########### Q2 - Toutes les entrées ###########

def best_infiltration():
    global couches, solution, chemin
    for ei in range(couches.shape[1]):
        chemin["Cellules"]=[]; chemin["Durée"]=0
        infiltration(0, ei)

    # test de la Q2            
#best_infiltration()

########### Q3 - Programmation dynamique ###########

def infiltration_dynamique():
    global couches
    durees=np.full(couches.shape, math.inf, dtype="int")
    durees[0,:]=couches[0,:]
    for c in range(1,couches.shape[0]):
        for ei in range(couches.shape[1]):
            for e in [ei-1, ei, ei+1] :
                if acceptable(e):
                    durees[c,ei]=min(durees[c,ei], durees[c-1,e]+couches[c,ei])
    return durees

    # test de la Q3            
durees=infiltration_dynamique()

########### Q4 - Recherche du chemin ###########

def parcours_infiltration(durees):
    global couches
    parcours=[]
    parcours.append(int(durees[-1,:].argmin()))
    for c in range(durees.shape[0]-2,-1,-1):
        pos=math.inf ; value=math.inf
        for e in [parcours[-1]-1, parcours[-1], parcours[-1]+1] :
            if (acceptable(e) and (durees[c,e]<value)) :
                    pos=e ; value=durees[c,e]
        parcours.append(pos) 
    return parcours

    # test de la Q4           
#parcours=parcours_infiltration(durees)
#parcours.reverse()
#print(parcours)