import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def p(n,s):
    pos=[0,0]
    for c in s:
        if c=='U':
            pos[1]+=1
        elif c=='D':
            pos[1]-=1
        elif c=='L':
            pos[0] -=1
        elif c=='R':
            pos[0] +=1
                    
        if pos[0]==1 and pos[1]==1:
            return "YES"
            
    return "NO"        
            
r=[]
for _ in range(ii()):
    n=ii()
    s=si()
    t=p(n,s)
    r.append(t)
    
for e in r:
    print(e)    