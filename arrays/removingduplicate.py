a=[1,2,2,3,3,4,4,5]
def appnd(a,el):
    c=[0 for _ in range(len(a)+1)]
    for i in range(len(a)):
        c[i]=a[i]
        i+=1
    c[-1]=el
    return c
def removedup(c):
    ar=[]
    ar=appnd(ar,c[0])
    for i in range(1,len(c)):
        if c[i]!=c[i-1]:
            ar=appnd(ar,c[i])
    return ar
print(removedup(a))