## exercice 3 ##
def conversion_masse (poids, unite, unite_conversion):
    unites = ["mg", "cg", "dg", "g", "dag", "hg", "kg"]
    unite_valide = False
    for u in unites:
        if u == unite:
            unite_valide = True
    if not unite_valide:
        return "unite invalide"
    else :
        for u in unites:
            if u == unite:
                index_unite = unites.index(u)
            if u == unite_conversion:
                index_unite_conversion = unites.index(u)
        if index_unite == index_unite_conversion:
            return poids
        if index_unite < index_unite_conversion:
            dif = index_unite_conversion - index_unite
            poids_converti = poids / (10 ** dif)
        else:
            dif = index_unite - index_unite_conversion
            print(dif)
            poids_converti = poids * (10 ** dif)
        
        return poids_converti
    
#print (conversion_masse(1, "kg", "g"))