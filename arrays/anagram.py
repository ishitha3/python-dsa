a='hasini'
b='inisha'
def is_anagram(a,b):
    if len(a) != len(b):
        return False
    c=["" for _ in range(len(a))]
    d=["" for _ in range(len(b))]
    for i in range(len(a)):
        c[i]=a[i]
    for i in range(len(b)):
        d[i]=b[i]
    c.sort()
    d.sort()
    for i in range(len(c)):
        if c[i]!=d[i]:
            return False
    return True
print(is_anagram(a,b))