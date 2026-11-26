#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec  8 19:32:29 2025

@author: pa_bisgambiglia
"""

import numpy as np
import random as rd
import copy
import math

"""----------------------------------------------
        Exercice 5 : Ordonnancement d'intervalles
   ----------------------------------------------"""
ordonnancement = np.loadtxt("Ordonnancement.txt", dtype=int)


########### Q1 - Ordonnanceùent récursive ###########

def acceptable(e):
    global ordonnancement, serie
    if serie["Value"]==0 : der=0
    else : der=serie["Intervalles"][-1]
    if (ordonnancement[e,1]>=ordonnancement[der,2]) : return True
    return False

def ordonnancement_recursive(ei):
    global ordonnancement, solution, serie
    if (ei==ordonnancement.shape[0]) :
        if serie["Value"]>solution["Value"] :
            solution=copy.deepcopy(serie)
        return
    if acceptable(ei):
        serie["Intervalles" ].append(ei)
        serie["Value"] += ordonnancement[ei,3]
        ordonnancement_recursive(ei+1)
        serie["Value"] -= ordonnancement[ei,3]
        serie["Intervalles" ].pop()
    ordonnancement_recursive(ei+1)

    # test de la Q1  
#solution={"Intervalles" : [], "Value" : 0}
#serie={"Intervalles" : [], "Value" : 0}          
#ordonnancement_recursive(1)

########### Q2 - Recherche des prédécesseurs ###########

def predecesseurs():
    global ordonnancement
    ordonnancement=np.c_[ordonnancement,[0]*ordonnancement.shape[0]]
    for N in range(1,ordonnancement.shape[0]):
        d=ordonnancement[N,1] ; pre=N-1
        while ordonnancement[pre,2]>d : pre-=1
        ordonnancement[N,4]=pre
    
    # test de la Q2            
#predecesseurs()
      
########### Q3 - Ordonnanceùent dynamique ###########

def ordonnancement_dynamique():
    global ordonnancement
    predecesseurs()
    optimum=[0]*(ordonnancement.shape[0])
    for N in range(1,ordonnancement.shape[0]) :
        pn=ordonnancement[N,4]; vn=ordonnancement[N,3]
        optimum[N]=max(optimum[N-1],optimum[pn]+vn)
    return optimum

    # test de la Q3         
#optimum=ordonnancement_dynamique()

########### Q4 - Recherche des intervalles ###########

def intervalles(N):
    global ordonnancement, optimum
    Liste_intervalles=[]
    while N>0 : 
        pre=int(ordonnancement[N,4])
        if optimum[N]>optimum[pre]:
            Liste_intervalles.append(N)
        N=pre
    return Liste_intervalles

    # test de la Q4        
#Liste_intervalles=intervalles(6)

"""----------------------------------------------
        Exercice 6 : Distance d'édition
   ----------------------------------------------"""

########### Q1 - Distance d'édition dynamique ###########

def distance_edition(Mot1, Mot2):
    Distance=np.zeros((len(Mot1)+1,len(Mot2)+1))
    for m in range(1,len(Mot1)+1) : Distance[m,0]=m
    for n in range(1,len(Mot2)+1) : Distance[0,n]=n
    for m in range(1,len(Mot1)+1) :
        for n in range(1,len(Mot2)+1) :
            Distance[m,n]=min(Distance[m-1,n]+1,Distance[m,n-1]+1)
            if Mot1[m-1]!=Mot2[n-1] :
                Distance[m,n]=min(Distance[m,n], Distance[m-1,n-1]+1)
            else :
                Distance[m,n]=min(Distance[m,n], Distance[m-1,n-1])
    return Distance

    # test de la Q1
#Distance=distance_edition("DISTANCE","DETENTES")


"""----------------------------------------------
        Exercice 7 : Plus longue sous suite
   ----------------------------------------------"""

########### Q1 - Plus longue sous suite récursive ###########

def PLSS_recursive(m, n):
    global Mot1, Mot2
    if (m==0) or (n==0) :
        return 0
    PLSS=max(PLSS_recursive(m-1,n), PLSS_recursive(m,n-1))
    plus=0
    if Mot1[m-1]==Mot2[n-1] : plus=1
    return max(PLSS, PLSS_recursive(m-1,n-1)+plus)
    
    # test de la Q1
#Mot1="DISTANCE"
#Mot2="DETENTES"
#PLSS=PLSS_recursive(6,6)

########### Q2 - Plus longue sous suite récursive avec enregistrement ###########
    
def memoire(m,n) :
    PLSS=np.full((m,n), -1, dtype="int")
    for i in range(m) : PLSS[i,0]=0
    for i in range(n) : PLSS[0,i]=0
    return PLSS

def PLSS_memoire(m, n):
    global Mot1, Mot2, PLSS
    if (m==0) or (n==0) :
        return 0
    if PLSS[m-1,n]!=-1 : V1=PLSS[m-1,n]
    else : V1=PLSS_memoire(m-1,n)
    if PLSS[m,n-1]!=-1 : V2=PLSS[m,n-1]
    else : V2=PLSS_memoire(m,n-1)
    if PLSS[m-1,n-1]!=-1 : V3=PLSS[m-1,n-1]
    else : V3=PLSS_memoire(m-1,n-1)
    if Mot1[m-1]==Mot2[n-1] : V3=V3+1
    PLSS[m,n]=max(V1,V2,V3)
    return PLSS[m,n]
    
    # test de la Q2
#Mot1="DISTANCE" ; Mot2="DETENTES"
#PLSS=memoire(len(Mot1)+1,len(Mot2)+1)
#PLSS_recursive_memoire(len(Mot2),len(Mot2))

########### Q3 - Plus longue sous suite récursive avec enregistrement (simplifié) ###########

def PLSS_simplifie(m, n):
    global Mot1, Mot2, PLSS
    if (m==0) or (n==0) :
        return 0
    if PLSS[m-1,n]!=-1 : V1=PLSS[m-1,n]
    else : V1=PLSS_simplifie(m-1,n)
    if PLSS[m-1,n-1]!=-1 : V3=PLSS[m-1,n-1]
    else : V3=PLSS_memoire(m-1,n-1)
    if Mot1[m-1]==Mot2[n-1] : V3=V3+1
    if (V1!=V3) : 
        PLSS[m,n]=max(V1,V3)
    else :
        if PLSS[m,n-1]!=-1 : V2=PLSS[m,n-1]
        else : V2=PLSS_simplifie(m,n-1)
        PLSS[m,n]=max(V1,V2,V3)
    return PLSS[m,n]

    # test de la Q3      
#Mot1="DISTANCE" ; Mot2="DETENTES"
#PLSS=memoire(len(Mot1)+1,len(Mot2)+1)
#PLSS_simplifie(len(Mot2),len(Mot2))

########### Q4 - Plus longue sous suite dynamique ###########

def PLSS_dynamique():
    global Mot1, Mot2
    PLSS=np.zeros((len(Mot1)+1, len(Mot2)+1))
    for m in range(1,len(Mot1)+1) :
        for n in range(1, len(Mot2)+1):
            plus=0
            if Mot1[m-1]==Mot2[n-1] : plus=1
            PLSS[m,n]=max(PLSS[m-1,n], PLSS[m,n-1], PLSS[m-1,n-1]+plus)
    return PLSS

    # test de la Q4
#Mot1="DISTANCE" ; Mot2="DETENTES"
#PLSS=PLSS_dynamique()


"""----------------------------------------------
        Exercice 8 : Découpe de la barre de métal
   ----------------------------------------------"""
   
prix=[0,2,5,6,11,13,15,17,21]

########### Q1 - Découpe dynamique ###########

def decoupe_dynamique():
    maxPrix=[0]*len(prix) 
    for n in range(1,len(prix)):
       maxPrix[n]=prix[n]
       for i in range(0,n+1):
           if (prix[i]+maxPrix[n-i])>maxPrix[n] :
               maxPrix[n]=prix[i]+maxPrix[n-i]
    return maxPrix

    # test de la Q1
#maxPrix=decoupe_dynamique()

########### Q2 - Découpe dynamique avec les coupes ###########

def decoupe():
    maxPrix=[0]*len(prix) 
    Coupe=[0]*len(prix)
    for n in range(1,len(prix)):
       maxPrix[n]=prix[n]
       Coupe[n]=n
       for i in range(0,n+1):
           if (prix[i]+maxPrix[n-i])>maxPrix[n] :
               maxPrix[n]=prix[i]+maxPrix[n-i]
               Coupe[n]=i
    return maxPrix, Coupe

def afficheCoupe(n): 
    global Coupe
    Taille=n
    while Taille>0: 
        print(Coupe[Taille])
        Taille=Taille-Coupe[Taille]

    # test de la Q2
#maxPrix, Coupe=decoupe()
#afficheCoupe(7)