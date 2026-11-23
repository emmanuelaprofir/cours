def occurence(x, L):
    cmpt = 0
    for elt in L:
        if elt==x:
            cmpt+=1
    return cmpt

def element_majoritaire(L, i=0,maj=0):
    if i>=len(L):
            return maj
    
    if occurence(L[i], L)>len(L)/2:
        if occurence(L[i], L)>maj:
            maj = occurence(L[i], L)
    
    return element_majoritaire(L, i+1, maj)

print(element_majoritaire([1,2,1,1,1,4]))