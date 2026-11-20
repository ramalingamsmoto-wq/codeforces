

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

n,a,b=mi()
vp=[]
for i in range(a+1,n+1,1):
    vp.append(i)
    
l=len(vp)
j=0
cnt=0
for i in range(l-1,-1,-1):
    if j>b:
        break
    else:
        cnt=cnt+1
        j=j+1 
           
print(cnt)    
        