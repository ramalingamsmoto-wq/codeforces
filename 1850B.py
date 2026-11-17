import sys

input = lambda: sys.stdin.readline().rstrip()

# Short aliases for common input types
ii = lambda: int(input())                    # Single integer
mi = lambda: map(int, input().split())       # Multiple integers (unpacking)
li = lambda: list(map(int, input().split())) # List of integers
si = lambda: input()                         # Single string
ls = lambda: input().split()                 # List of strings


def process(a):
    b=[]
    for tup in a:
        if tup[1]<=10:
            tup1=(tup[0],tup[2])
            b.append(tup1)
    max_tuple = max(b, key=lambda x: x[1]) 
    
    return max_tuple[0]    
            
res=[]
for _ in range(ii()):
    n=ii()
    responses=[]
    for i in range(n):
        a,b=mi()
        tup=(i+1,a,b)
        responses.append(tup)
    t=process(responses)
    res.append(t)  
    
for e in res:
    print(e)      
        