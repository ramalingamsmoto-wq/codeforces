import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

from collections import deque

def process(a,b,c):
    l1=[a,b,c,0]
    queue = deque()
    queue.append(l1)
    
    mx=-1
    while True:
        
        if len(queue)==0:
            break
        
        top=queue.popleft()
        v=top[0]*top[1]*top[2]
        if v> mx:
            mx=v
        a1=top[0]
        b1=top[1]
        c1=top[2]
        moves=top[3]
        
        if moves+1 <= 5:
            l1=[a1+1,b1,c1,moves+1]  
            l2=[a1,b1+1,c1,moves+1]  
            l3=[a1,b1,c1+1,moves+1]
            queue.append(l1)
            queue.append(l2)
            queue.append(l3)
            
    return mx
    

res=[]
for _ in range(ii()):
    a,b,c=mi()
    tans=process(a,b,c)
    res.append(tans)
    
for e in res:
    print(e)    