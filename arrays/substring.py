st="abcabcbb"
sub='ab'

def check(st,sub,i):
    temp=i
    for k in range(len(sub)):
        if st[i]!=st[k]:
            return-1
        i+=1
    return temp
for i in range(len(st)):
    j=0
    if sub[j]==st[i]:
        print(check(st,sub,i))
        j+=1