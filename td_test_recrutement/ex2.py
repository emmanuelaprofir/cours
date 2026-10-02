
"""
def sontAnagrammes(a,b):
    sorted_a = ''.join(sorted(a.lower()))
    sorted_b = ''.join(sorted(b.lower()))
    return sorted_a == sorted_b

def sontAnagrammes(a,b):
    l_a =[]
    l_b =[]
    sorted_a = ''.join(sorted(a.lower()))
    sorted_b = ''.join(sorted(b.lower()))
    if len(a)==len(b):
        cpmt = 1
        c = ""
        for char in a:
            if c == char:
                cpmt +=1
            else :
                l_a.append(cpmt)
                c=char
                cpmt=1
        l_a.append(cpmt)
        cpmt=1
        for char in sorted_b:
            if c == char:
                cpmt +=1
            else :
                l_b.append(cpmt)
                c=char
                cpmt=1
        l_b.append(cpmt) 
    else : return False
    if len(l_a)==len(l_b):
        for i in range (len(l_a)):
            if l_a[i]!=l_b[i]:
                return False
    return True"""

def sontAnagrammes(a,b):
    sorted_a = sorted(a.lower())
    sorted_b = sorted(b.lower())
    c_s_a = sorted_a.copy()
    c_s_b = sorted_b.copy()
    for elt in sorted_a:
        if elt.isalpha()==False:
            c_s_a.pop(c_s_a.index(elt))
    for elt in sorted_b:  
        if elt.isalpha()==False:
            c_s_b.pop(c_s_b.index(elt))
    sa=''.join(c_s_a)
    sb=''.join(c_s_b)            
    return sa == sb


print (sontAnagrammes("tse???t1234567890","TEST"))

