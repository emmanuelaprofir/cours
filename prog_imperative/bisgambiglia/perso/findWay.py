"""Recette du Backtracking :
    - conditions (if)
    - vérification des appels récursifs avans de les return
    - revenir en arrière si l'appel récursif n'est pas bon
    - condition d'arrêt
    """

labyrinthe = [
    ["S", 0, 1, 0, 0],
    [1,   0, 1, 0, 1],
    [0,   0, 0, 0, 1],
    [0,   1, 1, 0, 0],
    [0,   0, 0, "E", 0]
]
chemin = []
ok = [0,"E"]

def findWay(posL, posC):
    chemin.append((posL,posC))
    if labyrinthe[posL][posC]=="E":
        return True
    if posC < 4 and labyrinthe[posL][posC+1] in ok and (posL,posC+1) not in chemin:
        r = findWay(posL, posC+1)
        if r :
            return True
    if posC > 0 and labyrinthe[posL][posC-1] in ok and (posL,posC-1) not in chemin:
        r = findWay(posL, posC-1)
        if r :
            return True
    if posL < 4 and labyrinthe[posL+1][posC] in ok and (posL+1,posC) not in chemin:
        r = findWay(posL+1, posC)
        if r :
            return True
    if posL > 0 and labyrinthe[posL-1][posC] in ok and (posL-1,posC) not in chemin:
        r = findWay(posL-1, posC)
        if r :
            return True
    
    chemin.pop()
    return False

findWay(0,0)
print(chemin)