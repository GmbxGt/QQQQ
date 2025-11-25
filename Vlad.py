def encode(s):
    if len(s)>1:
        l,e='',''
        for a in range(len(s)-1):
            l+=s[a]
            if s[a]!=s[a+1]:
                if len(l)>1: l=str(len(l))+str(l[0])
                else: l=str(l[0])
                e+=l
                l=''
        if len(l)>0:
            if s[-1]==l[-1]:
                l+=str(s[-1])
                e+=str(len(l))+str(l[0])
            else:e+=str(s[-1])
        else:e+=str(s[-1])
        return e
    else:return s

def decode(z):
    if len(z)>1:
        m,k,cif='','','0123456789'
        for a in z:
            if a in cif:m+=str(a)
            else:
                if len(m)>0:
                    k+=int(m)*str(a)
                    m=''
                else:k+=str(a)
        return str(k)
    else:return z
