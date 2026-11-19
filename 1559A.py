import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(n,a):
    
    
    
    

res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    t=process(n,a)
    res.append(t)
    
for e in res:
    print(e)
        