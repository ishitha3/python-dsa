n=int(input())
a=list(map(str,input().split(' ')))[:n]


def palindrome(a):
  l=0
  r=len(a)-1
  for i in range(len(a)//2):
    if a[l]==a[r]:
      l+=1
      r-=1
      return 'it is palindrome'
  return 'it is not a palindrome'
print(palindrome(a))