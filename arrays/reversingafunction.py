n=int(input())
a=list(map(int,input().split(' ')))[:n]
def reverse(a):
    l=0
    r=len(a)-1
    while l<r:
        temp=a[l]
        a[l]=a[r]
        a[r]=temp
        l+=1
        r-=1
    return a
print(reverse(a))