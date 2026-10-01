a=[1,2,3,4,5]
def search(val,a):
    for i in range(len(a)):
        if a[i]==val:
            print(f"{val} is found at {i} index")
            return
    print(f"{val} is not found")
a=search(2,a)