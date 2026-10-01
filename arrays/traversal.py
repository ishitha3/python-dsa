a=[1,2,3,4,5]
def traversal(b):
  print('[',end="")
  for i in range(len(b)-1):
    print(b[i],end=", ")
  print(b[-1],end="]")
traversal(a)