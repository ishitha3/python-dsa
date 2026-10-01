a=[1,2,3,4,5]
def rs(val,a):
    temp=val
    c=[0 for i in range(len(a))]
    for i in range(0,len(a)-val):
        c[val]=a[i]
        val+=1
    val=temp
    j=0
    for i in range(len(a)-val,len(a)):
        c[j]=a[i]
        j+=1
    print(c)
a=rs(3,a)