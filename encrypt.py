def occ(char,n):
    c=0
    if char!='':
        for i in char:
            if i==n:
                c+=1
    return c
def val_k(char,n):
    if occ(char,n)%2==0:
        return occ(char,n)//2
    elif occ(char,n)%2==1:
        return occ(char,n)*2
def remp(char):
    l=""
    alpha="abcdefghijklmnopqrstvwxyzabcdefghijklmnopqrstvwxyz"
    for i in char:
        n=val_k(char,i)
        x=alpha.find(i)
        l+=alpha[x+n]
    return l.upper()
Word=input("what do you want to encrypt ?:")
print("The encrypted word is :",remp(Word))