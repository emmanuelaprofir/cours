import random as rd
import copy
import math

def fib_recursive(n):
    if (n==1) or (n==0) :
        return 1
    return fib_recursive(n-1)+fib_recursive(n-2)

    # test de la Q1 
#print(fib_recursive(10))

########### Q2 - Version récursive avec mémorisation ###########
def fib_memorisation(nb):
    fibonacci = {0 : 1, 1 : 1}      #Création des données initiales
    for i in range(nb):
        n=rd.randint(0, 20)         #Choix aléatoire des valeurs de fibonacci à calculer
        if n in fibonacci :
            print(f'{n:<5} : {fibonacci[n]:<10} : TRUE')
        else :
            fibonacci[n]=fib_recursive(n)
            print(f'{n:<5} : {fibonacci[n]}')

    # test de la Q2 
#fib_memorisation(20)

########### Q3 - Version dynamique  ###########
def fib_dynamique(n):
    fibonacci = [0]*(n+1)
    fibonacci[0]=1 ; fibonacci[1]=1
    for i in range(2,n+1):
        fibonacci[i]=fibonacci[i-1]+fibonacci[i-2]
    print(fibonacci[n])
        
    # test de la Q3 
#fib_dynamique(20)

"""----------------------------------------------
        Exercice 2 : Rendu des pièces
   ----------------------------------------------"""

########### Q1 - Algorithme glouton ###########
Pieces=sorted([1, 6, 5], reverse=True)              #Trie d'une liste en ordre décroissant

def rendu_glouton(somme):
    rendu={} ; ind=0
    while (somme>0) and (ind<len(Pieces)) :
        if somme>Pieces[ind] :
            rendu[Pieces[ind]]=somme//Pieces[ind]   #Nombre de Pièces[ind] à rendre
            somme=somme%Pieces[ind]                 #somme restante
        ind+=1
    if somme==0 : 
        for key, value in rendu.items() :
            print(f'Piece {key:<10} : {value}')
    else :
        print('Pas de rendu possible')

    # test de la Q1 
#rendu_glouton(10)

########### Q2 - Version récursive  ###########
solution={"Pieces" : {}, "Nombre" : math.inf, "Somme" : 0}
rendu={"Pieces" : {}, "Nombre" : 0, "Somme" : 0}

def rendu_recursive(ei):
    global solution, rendu, Pieces, somme
    #Test d'arret 1 - Un solution est trouvée
    if rendu["Somme"]==somme :
        if rendu["Nombre"]<solution["Nombre"] : solution=copy.deepcopy(rendu)
        return 
    #Test d'arret 2 - Pas de solution 
    if ei==len(Pieces) : return 
    #Traitement de la ei ième piece
    reste = (somme-rendu["Somme"])
    if reste>=Pieces[ei]:
        rendu["Pieces"][Pieces[ei]]=reste//Pieces[ei]
        rendu["Nombre"] += rendu["Pieces"][Pieces[ei]]
        rendu["Somme"] += Pieces[ei]*rendu["Pieces"][Pieces[ei]]
        rendu_recursive(ei+1)
        rendu["Nombre"] -= rendu["Pieces"][Pieces[ei]]
        rendu["Somme"] -= Pieces[ei]*rendu["Pieces"][Pieces[ei]]
        del rendu["Pieces"][Pieces[ei]]
    rendu_recursive(ei+1)

    # test de la Q2 
#somme=11    
#rendu_recursive(0)

########### Q3 - Version dynamique  ###########

def rendu_dynamique(somme):
    global optimum, Pieces
    optimum=[math.inf]*(somme+1)
    optimum[0]=0
    
    for N in range(1,somme+1):
        for pi in Pieces :
            if N>=pi : 
                optimum[N]=min(optimum[N], optimum[N-pi]+1)
    return optimum

    # test de la Q3
#optimum=rendu_dynamique(11)

########### Q4 - Version dynamique avec trace  ###########
def rendu_trace(somme):
    global optimum, Pieces
    optimum=[math.inf]*(somme+1)
    optimum[0]=0
    trace=[0]*(somme+1)

    for N in range(1,somme+1):
        for pi in Pieces :
            if N>=pi : 
                if optimum[N]>(optimum[N-pi]+1) :
                    trace[N]=N-pi
                optimum[N]=min(optimum[N], optimum[N-pi]+1)
    return optimum, trace

    # test de la Q4
#optimum, trace=rendu_trace(11)

########### Q5 - Affichage de la trace  ###########
def pieces_rendues(somme):
    global optimum, trace
    if optimum[somme]==math.inf : 
        print(f"il n'y a pas de solution pour une rendu de {somme} euros")
        return
    reste=somme
    while reste>0 :
        print(f'une pièce de {reste-trace[reste]} euros' )
        reste=trace[reste]
        
    # test de la Q4
#pieces_rendues(8)
