

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(a,b):
    if a==b:
        return [0,0]
    else:
        mx=max(a,b)    
        mn=min(a,b)
        me=mx-mn
        if mx%me==0:
            return[me,0]
        else:
            q1=mx//me
            ul=(q1+1)*me
            ll=q1*me
            d1=ul-mx
            d2=mx-ll
            return [me,min(d1,d2)] 


res=[]
for _ in range(ii()):
    a,b=mi()
    t=process(a,b)
    res.append(t)
    
for list1 in res:
    print(*list1)    