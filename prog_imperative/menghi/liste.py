def parcourir(liste,i=0):
    if i == len(liste):
        return i
    print(liste[i])
    parcourir(liste, i+1)

#print(parcourir([3,2,0]))

def transformer(liste):
    if liste == []:
        return []
    return [liste[0], 1]+ transformer(liste[1:])

#print(transformer([3,2,0]))

def concatener(liste, res=[]):
    if liste == []:
        return res
    else:
        for i in range(len(liste)):
            if isinstance(liste[i], list):
                return concatener(liste[i],res)
            else:
                res.append(liste[i])
                return concatener(liste[i:])
    return(res)

print(concatener([[3],[2],[1]]))
    