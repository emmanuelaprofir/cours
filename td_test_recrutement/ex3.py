def estBienParenthese(s):
    if len(s)==0:
            return True
    lst =r"()[]{}"
    fini = False
    i = 0
    while not fini:
        print (i)
        if i+1>len(s):
            fini = True
        print(s[i])
        if s[i] not in lst:
            s = s[:i:]
        i +=1
    print(s)
    if len(s)%2!=0:
        return False
    l = len(s)-1
    ok1 = True
    ok2 = True
    for i in range(l):
            if s[i]=="(":
                if s[l-i]!=")":
                    ok1=False
                if i%2==0:
                    if s[i+1]!=")":
                        ok2=False
                else :
                    ok2=False
            if s[i]=="[":
                if s[l-i]!="]":
                    ok1=False
                if i%2==0:
                    if s[i+1]!="]":
                        ok2=False
                else :
                    ok2=False
            if s[i]=="{":
                if s[l-i]!="}":
                    ok1=False
                if i%2==0:
                    if s[i+1]!="}":
                        ok2=False
                else :
                    ok2=False
    if not ok1 and not ok2:
        return False
    else:
        return True

#ça se voit il est nustrale et il a un gros égo

print(estBienParenthese(r"{[((aa))]}"))