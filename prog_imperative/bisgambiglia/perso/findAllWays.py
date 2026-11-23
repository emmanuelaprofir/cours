""" """

labyrinthe = [
    ["S", 0, 0, 0, 0],
    [1,   0, 1, 0, 1],
    [0,   0, 0, 0, 1],
    [0,   0, 1, 0, 0],
    [1,   0, 0, "E", 0]
]
chemin = []
chemins = []
ok = [0,"E"]

def findAllWays(posL, posC):
    chemin.append((posL,posC))
    if labyrinthe[posL][posC]=="E":
        chemins.append(chemin.copy())
    else :
        if posC < 4 and labyrinthe[posL][posC+1] in ok and (posL,posC+1) not in chemin:
            findAllWays(posL, posC+1) 
        if posC > 0 and labyrinthe[posL][posC-1] in ok and (posL,posC-1) not in chemin:
            findAllWays(posL, posC-1)
        if posL < 4 and labyrinthe[posL+1][posC] in ok and (posL+1,posC) not in chemin:
            findAllWays(posL+1, posC)
        if posL > 0 and labyrinthe[posL-1][posC] in ok and (posL-1,posC) not in chemin:
            findAllWays(posL-1, posC)
    chemin.pop()

def findBestAndWorseWay(ways):
    best = ways[0]
    worse = ways[0]
    for w in ways:
        if len(w) < len(best):
            best = w
        if len(w) > len(worse):
            worse = w
    return best, worse

findAllWays(0,0)
best, worse = findBestAndWorseWay(chemins)
print("Chemin le plus court :", len(best), best)
print("Chemin le plus long :", len(worse), worse)