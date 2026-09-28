def encode(jour, mois, annee):
    #bits = "0"*32
    jour = bin(jour)[2:]
    mois = bin(mois)[2:]
    annee = bin(annee)[2:]
    if len(annee)<=23:
        z = 23-len(annee)
        date = "0"*z+annee
    else :
        return "L'année est incorrecte"
    if len(mois)<=4:
        z = 4-len(mois)
        date = "0"*z+mois+date
    else :
        return "Le mois est incorrect"
    if len(jour)<=5:
        z=5-len(jour)
        date = "0"*z+jour+date
    else :
        return "Le jour est incorrect"

    return(date)

def decode(date):
    if len(date) != 32:
        return "La date en binaire est incorrecte"
    else :
        jour = int(date[:5],2)
        mois = int(date[5:9],2)
        annee = int(date[9:],2)
        return jour,mois,annee

#print(decode(encode(16,6,2026)))

def ip (ip):
    a = (ip >> 24) & 255
    b = (ip>>16) & 255
    c = (ip>>8) & 255
    d = ip & 255
    return (a,b,c,d)

#print(ip(1921681010))

print(bin(192))
print(bin(168))
print(bin(10))
print(int(11000000101010001010))