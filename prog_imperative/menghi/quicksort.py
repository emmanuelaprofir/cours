#pivot
def partition(T, g, d):
    bas = g 
    haut = d 
    pivot = g
    while bas < haut :
        if T[haut] < T[bas]:
            T[bas], T[haut] = T[haut], T[bas]
            pivot = bas + haut - pivot
        if pivot == haut:
            bas = bas +1
        else :
            haut = haut +1
    return pivot

#def tri_rapide
