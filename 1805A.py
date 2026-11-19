import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings

def process(n,a):
    
    v1=0
    for i in range(n):
        v1=v1^a[i]
    
    for i in range(n):
        a[i]=a[i]^v1
    
    v2=0    
    for i in range(n):
        v2=v2^a[i]
        
    if v2==0:
        return v1
    else:
        return -1        
            
        


res=[]
for _ in range(ii()):
    n=ii()
    a=li()
    t=process(n,a)
    res.append(t)
    
for e in res:
    print(e)    