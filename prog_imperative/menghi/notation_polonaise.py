#(5-6)x7 --> x(-56)7

def polonaise(calcul):
    operateurs =["+","-","*","/"]
    chiffres = ["0","1","2","3","4","5","6","7","8","9"]
    calcul = str(calcul)
    res = []
    for i in range(len(calcul)):
        if calcul[i] == "(":
            res.append(calcul[i])
            print(calcul[i+1:])
            polonaise(calcul[i+1:])
        if calcul[i] == "]":
            res.append(calcul[i])
        if calcul[i] in operateurs:
            res.insert(0,calcul[i])
    for i in range(len(calcul)):
        if calcul[i] in chiffres:
            res.append(calcul[i])
    return ''.join(res)



print(polonaise("(5-6)*7"))