a=[3,1,4,1,5,9,2,6]
def rangesumarray(a):
  ar=[]
  sum=0
  for i in a:
    sum+=i
    ar.append(sum)
  return ar
b=(rangesumarray(a))
print((b[5]-b[2-1]))
a=[3,1,4,1,5,9,2,6]
def prefixsumarray(a):
  ar=[]
  sum=0
  for i in a:
    sum+=i
    ar.append(sum)
  return ar
print(prefixsumarray(a))
a=[-1,5,3,2,1,0,7,6]
def sliding(key,a):
    sum=0
    for i in range(0,key):
        sum=sum+a[i]
    min=sum
    for i in range(key,len(a)):
        sum+=a[i]
        sum-=a[i-key]
        if min>sum:
            min=sum
    print(min)
a=sliding(2,a)
a=[-1,5,3,2,1,0,7,6]
def avgsliding(key,a):
    sum=0
    for i in range(0,key):
        sum=sum+a[i]
    minavg=sum/key
    for i in range(key,len(a)):
        sum+=a[i]
        sum-=a[i-key]
        avg=sum/key
        if minavg>avg:
            minavg=avg
    print(minavg)
a=avgsliding(2,a)
n=int(input())
a=list(map(int,input().split(' ')))[:n]
def maxVol(a):
    l=0
    r=len(a)-1
    max_volume=0
    for i in range(len(a)//2):
        height=min(a[l],a[r])
        width=r-l
        volume = height * width
        if volume > max_volume:
            max_volume = volume
        l += 1
        r -= 1
    return max_volume
print(maxVol(a))
a=[-1,5,3,2,1,0,7,6]
def sliding(key,a):
    sum=0
    for i in range(0,key):
        sum=sum+a[i]
    max=0
    for i in range(key,len(a)):
        sum+=a[i]
        sum-=a[i-key]
        if max<sum:
            max=sum
    print(max)
a=sliding(2,a)
c=[1,3,-1,-3,5,3,6,7]
li=[]
def append(c,el):
  a=[0 for _ in range(len(c)+1)]
  for i in range(len(c)):
    a[i]=c[i]
  a[-1]=el
  return a

def maximum_subarray(a,k):
    for i in range(k,len(a)+1):
        li.append(maximum(a,i-k,i))
    return li

def maximum(a,st,end):
    max=0
    for i in range(st,end):
        if max<a[i]:
            max=a[i]
    return max

print(maximum_subarray(c,3))
a=[-1,5,3,2,1,0,7,6]
def avgsliding(key,a):
    sum=0
    for i in range(0,key):
        sum=sum+a[i]
    maxavg=sum/key
    for i in range(key,len(a)):
        sum+=a[i]
        sum-=a[i-key]
        avg=sum/key 
        if maxavg<avg:
            maxavg=avg
    print(maxavg)
a=avgsliding(4,a)