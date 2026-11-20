

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def getf(a,b):
    v1=a*a
    v2=b*b
    v3=2*a*b
    v=v1+v2+v3
    return v

d=dict()
for i in range(0,101,1):
    for j in range(0,101,1):
        tv=getf(i,j)
        if tv not in d:
            d[tv]=[i,j]
            
def process(s):
    v=int(s)
    if v not in d:
        return [1]
    else:
        a,b=d[v]    
        return [0,a,b]
    

res=[]
for _ in range(ii()):
    s=si()
    t=process(s)
    res.append(t)

for list1 in res:
    if list1[0]==0:
        print(f"{list1[1]} {list1[2]}") 
    else:
        print(-1)    
    
    
    