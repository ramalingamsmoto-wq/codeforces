

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

res=[]
for _ in range(ii()):
    a,b,c=mi()
    fet=abs(a-1)
    set=abs(c-b)+abs(c-1)
    if fet<set:
        res.append(1)
    elif set<fet:
        res.append(2)   
    else:
        res.append(3)    

for e in res:
    print(e)        
         