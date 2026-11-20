

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()   
              # List of strings
from operator import itemgetter


def process(n,s):
    a=[]
    b=[0]*n
    for i in range(n):
        l1=[i,s[i]]
        a.append(l1)
    sa = sorted(a,key=itemgetter(1),reverse=True)   
     
    for i in range(n):
        if i!=sa[0][0]:
            v1=s[i]-sa[0][1]
            b[i]=v1
        else:
            v1=s[i]-sa[1][1]
            b[i]=v1
    return b        
            
    
res=[]
for _ in range(ii()):
    n=ii()
    s=li()
    tans=process(n,s)
    res.append(tans)

for list1 in res:
    print(*list1)    