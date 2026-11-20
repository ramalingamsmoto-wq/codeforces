import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


n,m=mi()
a=li()

q=deque()
i=1
for e in a:
    q.append([i,e])
    i=i+1
    

while True:
    
    l=len(q)    
    if l==1:
        break
    top=q.popleft()    
    
    if top[1]>m:
        v1=top[1]-m
        q.append([top[0],v1])

top=q.popleft()

print(top[0])     
        