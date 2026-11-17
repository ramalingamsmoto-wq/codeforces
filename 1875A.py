import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(a,b,n,x):
    x.sort()
    x.insert(0,b)
    l=len(x)
    aux=[0]*l
    aux[0]=x[0]-1
    for i in range(1,l,1):
        nt=1+x[i]
        if nt> a:
            nt=a
        aux[i]=nt-1  
    s=sum(aux)   
    return s+1  
        
        
res=[]
for _ in range(ii()):
    a,b,n=mi()
    x=li()
    t=process(a,b,n,x)
    res.append(t)
    
for e in res:
    print(e)    