

import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

from collections import deque

n,x=mi()

cc=x
dcnt=0
q = deque()
for _ in range(n):
    sign,v=ls()
    l1=[sign,int(v)]
    q.append(l1)
    
while True:
    if len(q)==0:
        break 
    else:
        top=q.popleft()  
        
        if top[0]=='+':
            cc=cc+top[1]
            
        else:
            
            if top[1]<=cc:
                cc=cc-top[1] 
                
            else:
                dcnt=dcnt+1   
                
                
print(f"{cc} {dcnt}")                  
    
    
