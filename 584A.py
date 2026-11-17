import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


n,t=mi()

if t<10:
    b=str(t)*n
    
    
    
else:
    
    nn=n-1
    b=str(0)*nn 
    b="1"+b
    
    
v1=int(b)    
if v1%t !=0:
    print(-1)
else:    
    print(b)    
    