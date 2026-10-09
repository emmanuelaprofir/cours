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
            haut = haut -1
    return pivot

def tri_rapide(T, g=0, d=None):
    if d is None:
        d=len(T)-1
    if g < d:
        p = partition(T,g,d)
        tri_rapide(T, g, p-1)
        tri_rapide(T,p+1, d)
    return T
T=[5,3,8,1,9,2,7]
print(tri_rapide(T))
