#exercice 4 autres modifs aaaaaa modification

#commit

def rendu_monnaie (somme_a_rendre : float, monnaie_a_disposition:list):
    rendu = []
    rendu_temp = []
    compteur = 0
    while compteur < 100:
        if somme_a_rendre == 0.00:
            compteur =100
        else:
            for monnaie in monnaie_a_disposition:
                if monnaie<= somme_a_rendre:
                    rendu_temp.append(monnaie)
        if rendu_temp:
            r=max(rendu_temp)
            rendu.append(r)
            somme_a_rendre -= r
            rendu_temp = []
        compteur += 1
    if somme_a_rendre > 0.00:
        print("Impossible de rendre la monnaie")
    else:
        rendu_final = {}
        for e in rendu:
            if e not in rendu_final:    
                rendu_final[e]=1
            else :
                rendu_final[e]+=1
        return rendu_final

print("Rendu de monnaie avec le nombre d'unités : ",rendu_monnaie(65.0,[10.0,50.0,0.5,10.0,5.0]))

#modifications

#blablabla